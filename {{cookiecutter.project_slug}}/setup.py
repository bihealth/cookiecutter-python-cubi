#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup, find_packages

import versioneer


def parse_requirements(path):
    """Parse ``requirements.txt`` at ``path``."""
    requirements = []
    with open(path, "rt") as reqs_f:
        for line in reqs_f:
            line = line.strip()
            if line.startswith("-r"):
                fname = line.split()[1]
                inner_path = os.path.join(os.path.dirname(path), fname)
                requirements += parse_requirements(inner_path)
            elif line != "" and not line.startswith("#"):
                requirements.append(line)
    return requirements


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

test_requirements = parse_requirements("requirements/test.txt")
install_requirements = parse_requirements("requirements/base.txt")

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email=("{{ cookiecutter.email }}"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # entry_points={"console_scripts": ("{{cookiecutter.project_slug|replace("_", "-")}} = {{cookiecutter.project_slug}}.__main__:main",)},
    description="{{ cookiecutter.project_short_description }}",
    install_requires=install_requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    # long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{cookiecutter.project_slug}}",
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(include=["{{cookiecutter.project_slug}}"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/bihealth/{{cookiecutter.project_slug}}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
