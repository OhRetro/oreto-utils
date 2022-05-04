import setuptools
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

setuptools.setup(
    name = "oreto-utils",
    version = "0.6",
    author = "OhRetro",
    author_email = "notarealemail@email.com",
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
    requires = ["PyQt5"],
    packages = setuptools.find_packages(where="."),
    python_requires = ">=3.6"
)