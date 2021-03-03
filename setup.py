# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dj12djdjs_erpnext_customizations/__init__.py
from dj12djdjs_erpnext_customizations import __version__ as version

setup(
	name='dj12djdjs_erpnext_customizations',
	version=version,
	description='Customize ERPNext.',
	author='Devin Slauenwhite',
	author_email='devin.slauenwhite@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
