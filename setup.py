from setuptools import setup, find_packages

setup(
    name="analysis_tools",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Reusable tools for data analysis",
    author="Your Name",
    license="MIT",
    install_requires=["ipython"],  # Add any dependencies here
)
