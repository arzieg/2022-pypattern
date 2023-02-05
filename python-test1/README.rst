========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-test1/badge/?style=flat
    :target: https://readthedocs.org/projects/python-test1
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/arzieg/python-test1.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/arzieg/python-test1

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/arzieg/python-test1?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/arzieg/python-test1

.. |requires| image:: https://requires.io/github/arzieg/python-test1/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/arzieg/python-test1/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/arzieg/python-test1/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/arzieg/python-test1

.. |version| image:: https://img.shields.io/pypi/v/test1.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/test1

.. |commits-since| image:: https://img.shields.io/github/commits-since/arzieg/python-test1/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/arzieg/python-test1/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/test1.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/test1

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/test1.svg
    :alt: Supported versions
    :target: https://pypi.org/project/test1

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/test1.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/test1


.. end-badges

test

* Free software: MIT license

Installation
============

::

    pip install test1

Documentation
=============


https://python-test1.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
