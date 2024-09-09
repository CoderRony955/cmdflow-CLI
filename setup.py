from setuptools import setup, find_packages

setup(
    name='cmdflow_CLI',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
           'cmdflow=cmdflow_CLI.CLI:main_entry_point',
        ],
    },
    install_requires=[
        'rich',
        'pyfiglet',
        'matplotlib',
        'asyncio',
        'psutil'
    ],
    author='Raunak',
    description='A CLI tool for system monitoring, making plot charts and etc.',
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
