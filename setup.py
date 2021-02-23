from setuptools import setup, find_packages

setup(
    name="potato",
    version="0.1",
    description="Potato demo application.",
    packages=find_packages(),
    install_requires=["gunicorn"],
)
