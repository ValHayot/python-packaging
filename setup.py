import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmb-v33hs", # Replace with your own username
    version="0.0.1",
    author="Valerie Hayot",
    author_email="valeriehayot@gmail.com",
    description="some very cool code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ValHayot/python-packaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "nibabel>=2.40",
        "numpy",
        "pillow"
    ],
    entry_points = {
        'console_scripts': ['cmb=cmb.run:main'],
    }
)
