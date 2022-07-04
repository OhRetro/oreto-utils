from setuptools import setup, find_packages
from os.path import join, dirname, abspath

current_directory = dirname(abspath(__file__))

try:
    with open(join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

setup(
    name = "oreto-utils",
    version = "0.9",
    author = "OhRetro",
    author_email = "notareal@email.com",
    description = "a bunch of utilities to use in my code without copying and pasting the function from code to code",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/OhRetro/oreto-utils",
    project_urls = {
        "GitHub": "https://github.com/OhRetro/oreto-utils",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    install_requires = ["PyQt5", "keyboard", "psutil"],
    packages = find_packages(where="."),
    python_requires = ">=3.7"
)