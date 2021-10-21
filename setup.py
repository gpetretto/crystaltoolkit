# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="crystal_toolkit",
    version="2021.10.21",
    python_requires="==3.*,>=3.8.0",
    author="Matthew Horton",
    author_email="mkhorton@lbl.gov",
    packages=[
        "crystal_toolkit",
        "crystal_toolkit.apps",
        "crystal_toolkit.apps.examples",
        "crystal_toolkit.apps.examples.tests",
        "crystal_toolkit.apps.tests",
        "crystal_toolkit.components",
        "crystal_toolkit.components.transformations",
        "crystal_toolkit.core",
        "crystal_toolkit.core.tests",
        "crystal_toolkit.helpers",
        "crystal_toolkit.renderables",
    ],
    package_dir={"": "."},
    package_data={
        "crystal_toolkit": ["*.json"],
        "crystal_toolkit.apps": [
            "assets/*.css",
            "assets/*.ico",
            "assets/*.json",
            "assets/*.png",
            "assets/fonts/*.eot",
            "assets/fonts/*.svg",
            "assets/fonts/*.ttf",
            "assets/fonts/*.woff",
            "assets/fonts/*.woff2",
        ],
        "crystal_toolkit.apps.examples": ["*.json"],
        "crystal_toolkit.core": ["*.yaml"],
    },
    install_requires=[
        "crystaltoolkit-extension==0.*,>=0.4.0",
        "mp-api",
        "mp-pyrho==0.*,>=0.0.21",
        "plotly==5.*,>=5.3.1",
        "pydantic",
        "pymatgen==2022.*,>=2022.0.14",
        "scikit-image",
        "scikit-learn",
        "webcolors",
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1",
            "dephell",
            "pre-commit",
            "pytest",
            "recommonmark",
            "sphinx",
            "sphinx-rtd-theme",
        ],
        "fermi": ["ifermi", "pyfftw"],
        "figures": ["kaleido==0.*,>=0.2.1"],
        "server": [
            "dash[testing]==2.*,>=2.0.0",
            "dash-daq",
            "dash-extensions",
            "dash-mp-components==0.*,>=0.3.44",
            "dscribe",
            "flask-caching",
            "gevent",
            "gunicorn",
            "habanero",
            "redis",
            "robocrys",
            "sentry-sdk",
        ],
        "vtk": ["dash-vtk==0.*,>=0.0.6"],
    },
)
