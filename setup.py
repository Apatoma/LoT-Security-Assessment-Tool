from setuptools import setup, find_packages

setup(
    name="IoT Security Assessment Tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Flask',
        'python-nmap',
    ],
)
