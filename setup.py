import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='Project Initializer',
    version='0.1',
    scripts=['initProject.py'],
    author="CodeRevenge",
    author_email="mas.arley2009@gmail.com",
    description="A basic project initializer for multiple lenguages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeRevenge/ProjectInitializer",
    classifiers=[
         "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
