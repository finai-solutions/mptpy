from setuptools import setup, find_packages

setup(
    name="mptpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="Python client for mpt server API",
    author="Mohab.M.Metwally",
    author_email="mohab-metwally@riseup.net",
    url="https://github.com/finai-solutions/mpt",
)
