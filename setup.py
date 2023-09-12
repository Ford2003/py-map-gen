from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='py-map-gen',
    version='0.1',
    author='Ford2003',
    author_email='tommyford28@gmail.com',
    description='A package for generating data for a world with a seed.',
    packages=find_packages(),
    requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant"
    ]
)
