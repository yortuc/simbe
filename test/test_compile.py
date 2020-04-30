import unittest
import sys

sys.path.append('..')
from compile import extract_context_from_content, render_template, \
    read_template_files, read_content_files, get_post_links


class TestCompile(unittest.TestCase):
    def test_extract_context_from_content(self):
        lines = [
            '@template: post.html',
            '@title: YOLO Object Detection',
            '# YOLO Object Detection'
        ]

        context = extract_context_from_content(lines)
        expected_context = {
            'template': 'post.html',
            'title': 'YOLO Object Detection',
            'content': '# YOLO Object Detection'
        }

        assert context == expected_context


    def test_render_template_variable_correctly(self):
        context = {
            'title': 'Example post'
        }
        template_content = '- <%title%> -'
        expected_output  = '- Example post -'
        output = render_template(context, template_content, [])
        assert expected_output == output


    def test_render_template_function_correctly(self):
        def print_hello():
            return 'hello'

        context = {
            'myfunc': print_hello
        }
        template_content = '<%myfunc%> world!'
        expected_output = 'hello world!'
        output = render_template(context, template_content, {})
        assert output == expected_output


    def test_render_template_file_import_correctly(self):
        context = {
            'title': 'Example post'
        }
        template_content = '<%title%> -- <%page_footer%>'
        expected_output  = 'Example post -- this is footer'
        template_files = {
            'page_footer': {'content':'this is footer'}
        }
        output = render_template(context, template_content, template_files)
        assert expected_output == output


    def test_get_post_links_correctly(self):
        content_files = {
            'about': {
                'context': {'title': 'about', 'date': '28-04-2020'},
                'file_name': 'about.md'
            },
            'index': {
                'context': {},
                'file_name': 'index.md'
            }
        }
        links = get_post_links(content_files)
        expected_links = [('about.html', 'about', '28-04-2020')]
        assert links == expected_links


