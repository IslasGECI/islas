from setuptools import find_packages, setup

setup(
    name="islas",
    version="0.1.1",
    packages=find_packages() ,
    include_package_data=True,
    install_requires = [
        "geoambiental @ git+https://github.com/IslasGECI/geoambiental.git@v0.1.0",
        "utm",
        "numpy"
    ]
)
