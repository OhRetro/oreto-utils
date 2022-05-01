from distutils.core import setup
from setuptools import find_packages
import os

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

setup(
	# Name of the package 
	name="oreto-utils",
	# Packages to include into the distribution 
	packages=find_packages("."),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version="0.5",
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license="MIT",
	# Short description of your library 
	description="a bunch of utilities to use in my code without copying and pasting the function from code to code",
	# Long description of your library 
	long_description=long_description,
	long_description_content_type="text/markdown",
	# Your name 
	author="OhRetro",
	# Your email 
	author_email="",
	# Either the link to your github or to your website 
	url="https://github.com/OhRetro/oreto-utils",
	# Link from which the project can be downloaded 
	download_url="",
	# List of keywords 
	keywords=["oreto-utils", "oreto", "utils"],
	# List of packages to install with this one 
	install_requires=["PyQt5"],
	# https://pypi.org/classifiers/ 
	classifiers=["Development Status :: 5 - Production/Stable"]
)
