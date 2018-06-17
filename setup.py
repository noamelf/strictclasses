from setuptools import setup

setup(
    name='strictclasses',
    version='0.1.0',
    url='https://github.com/noamelf/strictclasses',
    author='Noam Elfanbaum',
    author_email='noam.elf@gmail.com',
    description='A strict companion to dataclasses',
    packages=['strictclasses'],
    install_requires=['dataclasses'],
)
