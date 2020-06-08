import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="kbdextension",
    version="1.0.1",
    description='Extension for python-markdown that adds markdown syntax for the KBD HTML tag.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/RickTalken/kbdextension.git',
    author='Rick Talken',
    author_email='rick@talken.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    py_modules=["kbdextension"],  
    install_requires=["markdown>=3.0"],
)
