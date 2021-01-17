from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='my_data_analysis_utils',
    version='0.0.1',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    description='utility scripts for kaggle',
    author='Taichi Nakamura',
)

