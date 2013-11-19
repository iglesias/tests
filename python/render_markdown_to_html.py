#!/usr/bin/python

'''
This script depends on PyGithub. Install with

pip install PyGitHub

or see the documentation at http://jacquev6.github.io/PyGithub/.
'''

import urllib2
from github import Github

markdown = urllib2.urlopen('http://raw.github.com/shogun-toolbox/shogun/develop/README.md').read()
g = Github()
html = g.render_markdown(markdown)
