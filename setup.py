from setuptools import setup, find_packages

setup(
    name="bridge-documentation",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "sphinx==7.1.2",
        "sphinx-rtd-theme==1.3.0",
        "myst-parser==2.0.0",
    ],
    author="SatoshiLabs",
    author_email="support@satoshilabs.com",
    description="Official Bridge Documentation",
    keywords="security, bridge, documentation, hardware, wallet",
    url="https://home-site.readthedocs.io",
    project_urls={
        "Documentation": "https://home-site.readthedocs.io",
        "Source Code": "https://github.com/satoshilabs/bridge",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)