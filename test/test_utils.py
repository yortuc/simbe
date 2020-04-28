import unittest
import sys

sys.path.append('..')
from utils import extract_context_from_content, render_template


class TestUtils(unittest.TestCase):
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

    def test_render_template_correctly(self):
        context = {
            'title': 'Example post',
            'date': '28-04-2020',
            'content': 'YOLO'
        }
        template_content = '<%title%> - <%date%> : <%content%>'
        expected_output  = 'Example post - 28-04-2020 : YOLO'

        output = render_template(context, template_content, '\\template_default')

        assert expected_output == output
