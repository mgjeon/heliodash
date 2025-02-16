from setuptools import find_packages, setup

setup(
    name="heliodash",
    version="0.0.1",
    description="Heliosphere Dashboard (HelioDash) is an open-source tool for visualizing heliosphere-related data",
    author="Mingyu Jeon",
    author_email="mgjeon1999@gmail.com",
    url="https://github.com/mgjeon/heliodash",
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "matplotlib",
        "astropy[all]",
        "sunpy[all]",
        "ply",
        "beautifulsoup4",
    ],
    packages=find_packages(),
    python_requires=">=3.10",
)
