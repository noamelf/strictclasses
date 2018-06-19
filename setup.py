from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='strictclasses',
    version='0.1.4',
    url='https://github.com/noamelf/strictclasses',
    author='Noam Elfanbaum',
    author_email='noam.elf@gmail.com',
    description='A strict companion to dataclasses',
    packages=['strictclasses'],
    install_requires=['dataclasses'],
    extras_require={'dev': ['pytest']},
    long_description=long_description,
    long_description_content_type='text/markdown'
)
