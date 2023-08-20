from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in etos_theme_v13/__init__.py
from etos_theme_v13 import __version__ as version

setup(
	name="etos_theme_v13",
	version=version,
	description="customizations",
	author="ecs",
	author_email="info@erpcloud.systems",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
