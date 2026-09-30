from setuptools import find_packages
from setuptools import setup

setup(
    name='rwip_ros2_package',
    version='0.0.0',
    packages=find_packages(
        include=('rwip_ros2_package', 'rwip_ros2_package.*')),
)
