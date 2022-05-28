from setuptools import setup
from os.path import join
import os

project_name = "drone_sim"

requirements = open('requirements.txt').read().splitlines()

setup(
    name=project_name,
    version="0.1.0",
    url="https://github.com/SuhrudhSarathy/drone_sim",
    author="Suhrudh Sarathy",
    author_email="suhrudhsarathy@gmail.com",
    description="Light-weight Simulator for Drones",
    license="MIT",
    install_requires=requirements,
    packages=[
        project_name,
        join(project_name, "gym"),
        join(project_name, "sim"),
        join(project_name, "viz"),
        join(project_name, "control")
    ],
    zip_safe=True
)