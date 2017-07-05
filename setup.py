from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tcpflow',
    version='0.1.0',
    description='A wrapper to use the TcpFlow CLI',
    long_description=long_description,
    url='https://github.com/liftitapp/tcpflow.py',
    author='Michel Perez',
    author_email='michel.ingesoft@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tcp development utils cli',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    extras_require={
        'dev': [],
        'test': ['pytest'],
    },
    package_data={
        'sample': [],
    },
)
