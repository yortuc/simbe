import re
import os
from os import listdir
from os.path import isfile, join, isdir
import shutil  

from markdown import markdown


def read_file(path):
    file = open(path, 'r') 
    content = file.read()
    file.close()
    return content


def read_file_lines(path: str):
    file = open(path, 'r') 
    content = file.readlines()
    file.close()
    return content


def list_files_in_dir(dir_path):
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return files

def list_dirs_in_dir(dir_path):
    folders = [f for f in listdir(dir_path) if isdir(join(dir_path, f))]
    return folders


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def extract_context_from_content_file(content_path: str):
    return extract_context_from_content(read_file_lines(content_path))


def extract_context_from_content(lines: str):
    # collect variables now    
    # read lines, get the ones starting with
    context = {}
    content = []
    
    for line in lines:
        if line[0] == '@':
            name, val = line[1:].split(':')
            context[name] = val.strip()
        else:
            content.append(line)
    
    # content is also a variable in context
    context.update({
        'content': ''.join(content)
    })
            
    return context


def render_template(context, template_content, template_files, processed_templates=set()) -> str:
    # find <%SYMBOL%>
    symbols = re.findall(r"<\%(.*?)\%>", template_content)
    symbols = [k.replace('<%', '').replace('%>', '') for k in symbols]
    
    # resolve symbols with variables
    for symbol in symbols:
        tmp_key = f'{symbol}.html'
        # if symbol is a template file
        
        if tmp_key in template_files: 
            print(f'processing {tmp_key}')
            # read file content also render that template with context and replace
            # keep the track of processed template files to avoid circular dependencies
            # if this template file is already processed, there is a circular dep.
            # if tmp_key in processed_templates:
            #     raise Exception(f'There is a circular dependency in template files. \nAlready processed: {processed_templates}, still wants to import {tmp_key}')
            
            processed_templates.add(tmp_key)
            imported_template_content = render_template(
                context             = context, 
                template_content    = template_files[tmp_key]['content'], 
                template_files      = template_files, 
                processed_templates = processed_templates
            )
            template_content = template_content.replace(f'<%{symbol}%>', imported_template_content)
        
        elif symbol in context:
            # get val from context
            value = None
            
            if callable(context[symbol]): # if it's a function, call it
                value = context[symbol]()
            else:
                value = context[symbol]   # value

            template_content = template_content.replace(f'<%{symbol}%>', value)
        
        else:
            # throw error
            raise Exception(f'Symbol cannot be resolved in template. No file "{symbol}.html", No variable in content as "{symbol}"')
    
    return template_content


def read_template_files(template_folder):
    ret = {}
    template_files = list_files_in_dir(template_folder)
    
    for f in template_files:
        ret[f] = {
            'content': read_file(join(template_folder, f))
        }
    return ret


def read_content_files(content_folder):
    ret = {}
    content_files = list_files_in_dir(content_folder)

    for file in content_files:
        file_context = extract_context_from_content_file(join(content_folder, file))
        ret[file] = {
            'context': file_context,
            'file_name': file
        }
    return ret


def get_post_links(content_files):
    ret = []
    for f in content_files.keys():
        if 'title' in content_files[f]['context']:
            c = content_files[f]['context']
            fn = content_files[f]['file_name'].replace('.md', '.html')
            ret.append((fn, c['title'], c['date']))
    return ret


def render_post_links(post_links):        
    ret = ['<ul>']
    for p in post_links:
        ret.append(f'<li><a href="{p[0]}">{p[1]}</a> <span class="linkdate">{p[2]}</span></li>')
    ret.append('</ul>')
    return ''.join(ret)


def create_post_links_func(content_files):
    def post_links():
        return render_post_links(get_post_links(content_files))
    return post_links


def save_to_file(path, string):
    file = open(path, 'w') 
    content = file.write(string)
    file.close()


def compile(config):
    # get content files
    content_files = read_content_files(config['content_folder'])
    template_files = read_template_files(config['template_folder'])

    for c in content_files.keys():
        print(f'processing {c}')
        context = content_files[c]['context']
        context.update({
            'post_links': create_post_links_func(content_files),
            'content': markdown(context['content'], extensions=['codehilite'])
        })
        template_name = context['template']
        template_content = template_files[template_name]['content']
        
        output = render_template(
            context = context,
            template_content = template_content,
            template_files = template_files
        )
        output_file_path = join(config['output_folder'], content_files[c]['file_name'].replace('.md', '.html'))
        save_to_file(output_file_path, output)

    # copy all the folders and their content to output dir
    dirs = list_dirs_in_dir(config['content_folder'])
    print('dirs:', dirs)
    for d in dirs:
        src = join(config['content_folder'], d)
        dest = join(config['output_folder'], d)
        copy_and_overwrite(src, dest)


DEFAULT_CONFIG = {
    'template_folder': '.\\template_default',
    'content_folder' : '.\\posts',
    'output_folder'  : '.\\output'
}

if __name__ == "__main__":
    compile(DEFAULT_CONFIG)
