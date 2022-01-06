from setuptools import setup, find_namespace_packages
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()
requirements = open('requirements.txt').read().splitlines()
setup(
    # Define the library name
    name='Drone_Simulator',

    # Repository's author's name
    author='Suhrudh Sarathy',

    # Email id of the author
    author_email='suhrudhsarathy@gmail.com',

    # URL to thr repository
    url='https://github.com/SuhrudhSarathy/drone_sim.git',

    # A short desciprtion to the package
    description='A simple drone dynamics simulation written in python.',
    long_description=long_description,

    # Defined all the packages to be installed
    packages=find_namespace_packages(include=['drone_sim.*']),

    # Defined as Major Version=0, Minor-Version=1, Maintainance-version=0
    version='0.1.0',

    # the library required in order to run
    install_requires=requirements,

    # includes all the data in the package folder
    include_package_data=True,
)
