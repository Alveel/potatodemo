from setuptools import setup, find_packages

setup(
    name="potatodemo",
    version="0.1",
    description="Potato demo application.",
    packages=find_packages(),
    install_requires=["gunicorn"],
)
