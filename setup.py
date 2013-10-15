#!/usr/bin/python
#encoding:utf-8
""" Installer Setup config file"""

from distutils.core import setup


setup(
    name = 'cmds',
    version = '1.0',
    packages = ['cmds'],
    scripts = commands,
    license = 'MIT',
    description = 'command line commands, with autcompletion with bash',
    long_description=open('README').read()
)
