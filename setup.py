from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cool-commits',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.1',

    description="Find the coolest git commits' hashes in your project!",
    long_description=long_description,

    url='https://github.com/OrDuan/cool_commits',

    # Author details
    author='Or Duan',
    author_email='orduani@gmail.com',

    # Choose your license
    license='Apache Software License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',

    # What does your project relate to?
    keywords='git cool commits hashes ',

    entry_points={
        'console_scripts': [
            'cool_commits=cool_commits:fin3d',
        ],
    },

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
)
