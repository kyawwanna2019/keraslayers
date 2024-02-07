from setuptools import setup, find_packages

setup(
    name='keraslayers',
    version='0.1',
    packages=find_packages(),
    author='',
    author_email='',
    description='Keras models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT', 
    url="https://github.com/kyawwanna2019/keraslayers",
    install_requires=[
        'numpy',
        'tensorflow',
        'keras',
    ]
)
