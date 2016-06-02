try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='everware-cli',
      version='0.0',
      description='Command-line client for Everware',
      scripts=['bin/evrwr.py'])
