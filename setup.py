from setuptools import setup, find_packages

import xlrd


setup(
    name='xlrd-formulas',
    packages=find_packages(),
    include_package_data=True,
    version=xlrd.__version__,
    description='xlrd but with formulas',
    long_description='',
    author=xlrd.__author__,
    author_email='',
    url='',
    install_requires=[],
    zip_safe=False,
)
