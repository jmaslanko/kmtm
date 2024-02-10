from setuptools import setup

setup(
    name='kmtm',
    version='0.1.0',
    py_modules=['kmtm'],
    author='Jeremy Maslanko',
    description='Simple tool to convert kilometers/miles.',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'kmtm = kmtm.cli:cli',
        ],
    },
)