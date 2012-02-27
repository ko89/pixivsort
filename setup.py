try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A script for sorting pixiv images.',
    'author': 'Stefan Bernstein',
    'url': 'none',
    'download_url': 'none',
    'author_email': 's67762@informatik.htw-dresden.de',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pixivsort'],
    'scripts': [],
    'name': 'pixivsort'
}

setup(**config)
