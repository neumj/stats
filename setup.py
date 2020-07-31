from setuptools import setup, find_packages

reqs = [
    "matplotlib",
    "numpy",
    "pandas",
    "scipy",
    "yaml"
]

conda_reqs = [
    "matplotlib",
    "numpy",
    "pandas",
    "scipy",
    "yaml"
]

test_pkgs = []

setup(
    name="stats",
    python_requires='>3.4',
    description="Python package for stats refesher",
    url="https://github.com/neumj/stats",
    install_requires=reqs,
    conda_install_requires=conda_reqs,
    test_requires=test_pkgs,
    packages=find_packages(),
    include_package_data=True
)
