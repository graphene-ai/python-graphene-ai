# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('graphene/graphene.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "graphene",
    packages = ["graphene"],
    entry_points = {
        "console_scripts": ['graphene = graphene.graphene:main']
        },
    version = '0.1',
    description = "Graphene AI API.",
    long_description = long_descr,
    author = "Francis Bautista",
    author_email = "francis.bautista07@gmail.com",
    keywords = ['GRAPHENE', 'AI', 'NATURAL LANGUAGE PROCESSING', 'MULTILINGUAL'],
    url = "https://github.com/graphene-ai/python-graphene-ai",
    install_requires=[
        'argparse'
    ],
    install_requires=[            # I get to this in a second
          'urllib'
      ],
)