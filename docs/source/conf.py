from datetime import date

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Smart Powermeter'

author = 'J.G.Aguado'
email = 'jon-garcia@hotmail.com'

release = 'R1'
version = 'V2'

today = date.today()
compile_date = today.strftime("%B %d, %Y")

# -- Project information

rst_epilog  = """
.. |Product| replace:: %s
.. |Author| replace:: %s
.. |Email| replace:: %s
.. |Version| replace:: %s%s
.. |Date| replace:: %s
""" % (project, author, email, version, release, compile_date)


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.mathjax',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'numpydoc'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}
html_context = {}

html_logo = "images/logo/White.png"
html_show_sourcelink = True
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('my_theme.css')