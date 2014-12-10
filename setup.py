from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='systematrix_website',
    version=version,
    description='Appp for managing  website',
    author='Systematrix',
    author_email='info@systematrix.co.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
