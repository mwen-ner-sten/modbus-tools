#!/usr/bin/env python
"""
Setup script for the Modbus Simulator package.
"""

from setuptools import setup, find_packages
from modbus_simulator import __version__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="modbus-simulator",
    version=__version__,
    author="Modbus Simulator Team",
    author_email="example@example.com",
    description="A Python-based Modbus simulator and testing toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/modbus-simulator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pymodbus==2.5.3",
        "PyQt5>=5.15.2",
        "Twisted>=24.11.0",
        "pyserial>=3.5",
    ],
    entry_points={
        "console_scripts": [
            "modbus-simulator=modbus_simulator.__main__:main",
            "modbus-server=modbus_simulator.cli.server_cli:main",
            "modbus-client=modbus_simulator.cli.client_cli:main",
            "modbus-test=modbus_simulator.tests.test_modbus:run_full_test",
        ],
    },
) 