'''Civil Engineering'''
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requires = ['astropy'

]

setup(
    name='Civil Engineering',
    version='0.0.0.0',
    description='create entity for civil engineering',
    long_description=long_description,
    author='chenmich',
    author_email='403189920@qq.com',
    install_requires=requires
)
