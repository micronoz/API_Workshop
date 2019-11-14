from setuptools import find_packages
from setuptools import setup

setup(
    name='demo_app',
    version='1.0.0',
    license='BSD',
    description='Basic library book tracker.',
    packages=find_packages(),
    install_requires=['flask', 'gunicorn', 'flask-restful', 'requests', 'requests-async'],
)
