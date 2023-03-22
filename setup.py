#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    author="Jordan Keith",
    author_email='zedd_D1abl0@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Application list plugin for NetBox",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='netbox_application_list_plugin',
    name='netbox_application_list_plugin',
    packages=find_packages(include=['netbox_application_list_plugin', 'netbox_application_list_plugin.*']),
    test_suite='tests',
    url='https://github.com/zeddD1abl0/netbox_application_list_plugin',
    version='0.1.0',
    zip_safe=False,
)
