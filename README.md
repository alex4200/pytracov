# pytracov
The python pytest-tox-travis-codecov example repository!
## Goal
This repo is an example repository showing how to setup your code using **py**test, **t**ox, t**ra**vis and code**cov**.
# Tools
The used tools explained very briefly. 
## pytest
`pytest` is a framework for building simple and scalable tests. 
Excessive documentation [HERE](https://docs.pytest.org/en/stable/contents.html).

In the example it just defines some very simple unit tests of the defined functions.

## tox
`tox` is a generic virtualenv management and test command line tool you can use for running tests in different environments, checking package installation. Excessive documentation [HERE](https://tox.readthedocs.io/en/latest/).

In the example this tool is used in `travis` to run the `pytest` command

## travis
[travis](https://travis-ci.org/) is a continuous integration (CI) tool to test and deploy code. Excessive documentation [HERE](https://docs.travis-ci.com/).

In the example it is used to run the unit tests whenever a pull request is created (with results feed back to github).

## codecov.io
[codecov.io](https://codecov.io/) is a service providing highly integrated tools to group, merge, archive, and compare coverage reports. Excessive documentation [HERE](https://docs.codecov.io/docs).

In the example it is used to create a graphical overview of the coverage (especially useful when working with mnore complex code), and to provide the coverage badge.


# Setup

## Repository setup
The repository contains example files for the setup of the tools. The relevant files are `.travis.yml`, `tox.ini` and `setup.py`. 

You can check the `tox` setup by running the command `tox -e py36` in the top level of the repo. It should run the tests and create a coverage report (which, for educational reasons, are not at 100%). 

## Service setup

### travis
To setup the travis service, you have to do the following:

TBD
### codecov 
To setup the codecov service, you have to do the following:

TBD
