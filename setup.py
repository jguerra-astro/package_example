from setuptools import find_packages, setup

setup(
    name="scipackage",
    packages=find_packages(where="scipackage"),
    package_dir={"": "."},
)