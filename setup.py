from distutils.core import setup
from setuptools import find_packages


setup(
    name='chuck-norris-python',
    version='1.0',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    license='MIT',
    long_description='Python wrapper for "The Internet Chuck Norris Database" http://www.icndb.com/api/',
    install_requires=['requests'],
    url='https://github.com/Keda87/chuck-norris-python',
    author='Adiyat Mubarak',
    author_email='adiyatmubarak@gmail.com'
)
