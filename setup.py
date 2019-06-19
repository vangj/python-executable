import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name='my-app',
    version='1.0.0',
    description='Just do it!',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/bechtel/my-app',
    author='Team BDAC',
    author_email='bdac@bechtel.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=['my-app'],
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["my-app=doit:main"]}
)