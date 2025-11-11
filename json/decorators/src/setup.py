    from setuptools import setup, find_packages

    setup(
        name='decorators',
        version='0.1.0',
        packages=find_packages(),
        author='Gary Powell'
        author_email='gwpowell@gmail.com,
        description='basic use of custom python types for JSON',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/DoryGuy/PythonUtilites/tree/main/json/decorators', # Optional
        install_requires=[
            # List any dependencies here, e.g., 'requests>=2.20.0'
        ],
    )
