"""setup.py: setuptools control."""
from setuptools import setup, find_packages

setup(
    name='kake',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],  # Add your dependencies here
    entry_points={
        'console_scripts': [
            'kake=kake:main_function',
        ],
    },
)
