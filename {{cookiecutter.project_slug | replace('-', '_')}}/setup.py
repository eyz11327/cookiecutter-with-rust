#!usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as reqs:
    requirements = reqs.readlines()

setup(
    name = "{{ cookiecutter.project_slug }}",
    version = "0.0.0",
    description = "{{ cookiecutter.project_description }}",
    author = "{{ cookiecutter.project_author }}",
    install_requires = requirements,
    author_email = "{{ cookiecutter.project_email }}",
    packages = find_packages(),
    scripts = []
)