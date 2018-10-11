from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split()

setup(
    name="tweakstream",
    version="0.0.1",
    description="Tweakers topic streamer",
    python_requires=">=3.6.0",
    long_description=readme,
    entry_points={"console_scripts": ["tweakstream = tweakstream.cli:cli"]},
    license=license,
    install_requires=requirements,
    packages=find_packages(),
)
