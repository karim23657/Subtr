import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "subtr",
    version = "0.1",
    description = "Effortless Subtitle Translation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = ['subtr'],
    python_requires = ">=3.6",
    install_requires=[
       "requests",
       "pysrt",
   ],
)
