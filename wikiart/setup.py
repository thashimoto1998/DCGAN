"""WikiArt Retriever.

Author: Claud Monet -- <ld492@drexel.edu>
License: MIT License (c) 2016

"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='wikiart',
    description='Data fetcher and converter for art and metadata in '
                'http://wikiart.org/.',
    entry_points={
        'console_scripts': [
            'wikiart = wikiart.console:main',
        ]
    },
    long_description=open('README.md').read(),
    version='1.0.1',
    packages=['wikiart'],
    scripts=[],
    author='Claud Monet',
    author_email='lucasolivdavid@gmail.com',
    url='https://github.com/claudmonet/wikiart-retriever',
    download_url='https://github.com/claudmonet/wikiart-retriever/'
                 'archive/master.zip',
    install_requires=['requests'],
)
