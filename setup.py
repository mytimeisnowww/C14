from setuptools import setup, find_packages

setup(
    name='library_system',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'library_system = library_system:main',
        ],
    },
)


