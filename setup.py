#!/usr/bin/env python

from setuptools import setup, find_packages
import os


README = None
with open(os.path.abspath('README.md')) as fh:
    README = fh.read()

setup(
    name='py-chatbot',
    version='0.1.0',
    description=README,
    author='Ming Khoi',
    author_email='mingkhoitran1234@gmail.com',
    url='http://www.flask.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
     package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.html"],
    },
    install_requires=[
        'APScheduler',
        'Flask',
        'Flask-Bootstrap',
        'Flask-Cors',
        'Flask-REST-JSONAPI',
        'Flask-Restless',
        'Flask-SQLALchemy',
        'Flask-Script',
        'Flask-Security',
        'backoff',
        'configobj',
        'gunicorn',
    ],
    entry_points = {
        'console_scripts': [
            'flask-skeleton=flaskskeleton.controller:main',
            'flask-skeleton-worker=flaskskeleton.worker:main',
        ],
    }
)
