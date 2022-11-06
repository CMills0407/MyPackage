from setuptools import setup, find_packages

setup(
    name = 'MyPackage',
    version = '0.1',
    packages = find_packages(exclude=['Tests*']),
    license = 'MIT',
    description = 'EDSA example python package',
    long_description = open('Readme.md').read(),
    install_requires = ['numpy'],
    url = 'http://github.com/<username>/<package-name>',
    author = 'Christopher Mills',
    author_email = 'christopher.mills@merchantscx.com'
)