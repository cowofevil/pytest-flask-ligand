===================
pytest-flask-ligand
===================

Pytest fixtures and helper functions to use for testing flask-ligand microservices.

Developer Quick Start Guide
---------------------------

Follow the instructions below to get a development environment up and running quickly!

Prerequisites
=============

- Python 3.10+ (3.11 recommended)
- virtualenvwrapper_

Getting Help with Make Tasks
============================

Execute the following command to get a full list of ``make`` tasks::

    $ make help

Setup Python Development Environment
====================================

1. Create a Python virtual environment::

    $ mkvirtualenv -p py39 pytest-flask-ligand

2. Setup develop environment::

    $ make develop-venv

3. Verify that environment is ready for development::

    $ make test-all

Contributing
------------

See `CONTRIBUTING.rst`_ for more details on developing for the ``pytest-flask-ligand`` project.

Release Process
---------------

See `release_process.rst`_ for information on the release process for the ``pytest-flask-ligand`` project.

Python Black IDE Integration
----------------------------

This repo utilizes `Python Black`_ for automatic code formatting using the ``make format`` task. However, this is not
very convenient to use on a regular basis and instead it is recommended to integrate Python Black into your IDE
workflow. Checkout these `editor integration`_ guides for integrating `Python Black`_ with popular IDEs and text
editors.

.. _CONTRIBUTING.rst: CONTRIBUTING.rst
.. _release_process.rst: docs/release_process.rst
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _Python Black: https://black.readthedocs.io/en/stable/
.. _editor integration: https://black.readthedocs.io/en/stable/integrations/editors.html
