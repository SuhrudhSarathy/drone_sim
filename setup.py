from setuptools import setup
from os.path import join
import os

project_name = "drone_sim"

setup(
    name=project_name,
    version="0.1.0",
    url="https://github.com/SuhrudhSarathy/drone_sim",
    author="Suhrudh Sarathy",
    author_email="suhrudhsarathy@gmail.com",
    description="Light-weight Simulator for Drones",
    license="MIT",
    packages=[
        project_name,
        join(project_name, "gym"),
        join(project_name, "sim"),
        join(project_name, "viz"),
    ],
    zip_safe=True
)