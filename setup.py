from setuptools import setup

setup(
    name='kmtm',
    version='0.1.0',
    py_modules=['kmtm'],
    author='Jeremy Maslanko',
    author_email='maslankoj@gmail.com',
    url='https://github.com/jmaslanko/kmtm',
    description='Simple tool to convert kilometers/miles.',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        ],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'kmtm = kmtm.cli:cli',
        ],
    },
)