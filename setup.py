try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A script for sorting pixiv images.',
    'author': 'ko89',
    'url': 'none',
    'download_url': 'none',
    'author_email': 'ko89@posteo.de',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['pixivsort'],
    'scripts': [],
    'name': 'pixivsort'
}

setup(**config)
