import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-onix",
    version="0.0.2",
    author="Ömer Boratav",
    author_email="omerboratav@gmail.com",
    description="Dataclasses for EDItEUR's ONIX standards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oboratav/python-onix",
    project_urls={
        "Bug Tracker": "https://github.com/oboratav/python-onix/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)