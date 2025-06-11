from setuptools import setup, find_packages

setup(
    name="evolutionary-tree-analyzer",
    version="1.0.0",
    author="Mae Warner",
    author_email="biology.mae@gmail.com",
    description="Build and visualize phylogenetic trees from FASTA files using parsimony and ML-style methods.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/B10ma3/evolutionary-tree-analyzer",
    packages=["src"],
    package_dir={"src": "src"},
    include_package_data=True,
    install_requires=[
        "dash",
        "dash-bootstrap-components",
        "biopython",
        "matplotlib",
        "flask"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "tree-analyzer=app:main"
        ]
    }
)
