#coding: utf-8

from setuptools import setup, find_packages


setup(
    name='python-cielo',
    version='0.0.1',
    description='python api to Cielo Webservice 1.5',
    long_description=open("README.md").read(),
    author=u'Maurício Fagundes',
    author_email='mauricio.fagundes@gmail.com',
    url='http://github.com/mfagundes/python-cielo',
    install_requires=open("requirements.txt").read().split("\n"),
    packages=find_packages(),
    package_dir={"cielo": "cielo"},
)
