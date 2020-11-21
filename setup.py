import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cuttpy",
    version="1.1.1",
    author="IAmThe2ndHuman",
    license="MIT",
    description="Wrapper for the cutt.ly URL shortener API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IAmThe2ndHuman/cuttpy",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
