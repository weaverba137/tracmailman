from setuptools import setup


PACKAGE = 'TracMailman'
VERSION = '1.0.0.dev1234'
SUMMARY = 'A Trac plugin integrating searching of Mailman archives'
AUTHOR = 'Theron Ji, Spencer Fang, Benjamin Weaver'
EMAIL = 'benjamin.weaver@noirlab.edu'


setup(name=PACKAGE,
      version=VERSION,
      description=SUMMARY,
      author=AUTHOR,
      author_email=EMAIL,
      packages=['tracmailman'],
      package_data={PACKAGE : ['templates/*.html']},
      entry_points={'trac.plugins': 'tracmailman.web_ui = tracmailman.web_ui'},)
