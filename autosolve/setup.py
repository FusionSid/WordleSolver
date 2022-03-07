from setuptools import setup

APP = ['autosolve.py']
DATA_FILES = ["words.json"]
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
