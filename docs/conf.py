import sys

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': (f'https://docs.python.org/{sys.version_info[0]}.{sys.version_info[1]}', None),
    'pytest': ('https://docs.pytest.org/en/stable/', None),
}
nitpick_ignore = [
    ('py:class', 'module'),
    ('py:class', 'Function'),
]
