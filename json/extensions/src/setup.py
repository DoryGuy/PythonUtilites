""" Setup """
# pylint: disable=consider-using-with
from setuptools import setup, find_packages

setup(
    name='extensions',
    version='0.1.0',
    packages=find_packages(),
    author='Gary Powell',
    author_email='gwpowell@gmail.com',
    description='basic use of custom python types for JSON',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DoryGuy/PythonUtilites/tree/main/json/extensions', # Optional
    install_requires=[
        # List any dependencies here, e.g., 'requests>=2.20.0'
    ],
)
