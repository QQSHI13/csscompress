import unittest

##
# Copyright (c) 2013 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from csscompress.tests.base import BaseTest


class Tests(BaseTest):
    def test_issue_108(self):
        # https://github.com/yui/yuicompressor/issues/108

        input = '''
            table thead tr td {
                color: #CEDB00;
                padding: 0.5em 0 1.0em 0;
                text-transform: uppercase;
                vertical-align: bottom;
            }
        '''

        output = '''table thead tr td{color:#cedb00;padding:.5em 0 1.0em 0;text-transform:uppercase;vertical-align:bottom}'''

        self._test(input, output)

    def test_issue_59(self):
        # https://github.com/yui/yuicompressor/issues/59

        input = '''
            .issue-59 {
                width:100%;
                width: -webkit-calc(100% + 30px);
                width: -moz-calc(100% + 30px);
                width: calc(100% + 30px);
            }
        '''

        output = '''.issue-59{width:100%;width:-webkit-calc(100% + 30px);width:-moz-calc(100% + 30px);width:calc(100% + 30px)}'''

        self._test(input, output)

    def test_issue_81(self):
        # https://github.com/yui/yuicompressor/issues/81

        input = '''
            .SB-messages .SB-message a {
                color: rgb(185, 99, 117);
                border-bottom: 1px dotted text-shadow: 0 1px 0 hsl(0, 0%, 0%);
                text-shadow: 0 1px 0 hsla(0, 0%, 0%, 1);
            }
        '''

        output = '.SB-messages .SB-message a{color:#b96375;border-bottom:1px dotted text-shadow:0 1px 0 hsl(0,0%,0%);text-shadow:0 1px 0 hsla(0,0%,0%,1)}'

        self._test(input, output)


class TestDataUriWhitespace(unittest.TestCase):
    """Regression: whitespace inside url(data:...) must be preserved."""

    def test_svg_data_uri_keeps_spaces(self):
        from csscompress import compress
        css = ".a{background:url(\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path d='M 1 1 L 2 2'/></svg>\")}"
        out = compress(css)
        assert "M 1 1 L 2 2" in out, out

    def test_normal_urls_still_minified(self):
        from csscompress import compress
        css = ".a { background: url(https://example.com/a.png); color: #ff0000; }"
        out = compress(css)
        assert out == ".a{background:url(https://example.com/a.png);color:red}", out
