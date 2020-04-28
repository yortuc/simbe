import re


CONFIG = {
    template_folder : '.\\template_default',
    content_folder  : '.\\posts',
    output_folder   : '.\\output'
}


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


def extract_context_from_content_file(content_path: str):
    return extract_context_from_content(read_file_lines(content_path))


def extract_context_from_content(lines: str):
    # collect variables now    
    # read lines, get the ones starting with
    context = {}
    content = []
    
    for line in lines:
        if line[0] == '@':
            print(line)
            name, val = line[1:].split(':')
            context[name] = val.strip()
        else:
            content.append(line)
    
    # content is also a variable in context
    context.update({
        'content': ''.join(content)
    })
            
    return context


def render_template(context, template_content, template_folder):
    # template_path = join(self.template_folder, context['template'])
    
    # check if template exists
    # if not os.path.isfile(template_path):
    #     raise Exception(f'Template {template_path} cannot be found in {self.template_folder} for {self.content_path}')
        
    # template_content = self.get_file_content(template_path)
    
    # find <%SYMBOL%>
    symbols = re.findall(r"<\%(.*?)\%>", template_content)
    symbols = [k.replace('<%', '').replace('%>', '') for k in symbols]
    
    # resolve symbols with variables
    for symbol in symbols:
        # if symbol is file
        file_path = f'{template_folder}\\{symbol}.html'
        if os.path.isfile(file_path):
            # read file content and replace
            template_content = template_content.replace(f'<%{symbol}%>', read_file(file_path))
        
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
            raise Exception(f'Symbol cannot be resolved. No file "{file_path}", No variable in content as "{symbol}"')
    
    return template_content
