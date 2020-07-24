# pytracov
The python pytest-tox-travis-codecov example repository!

[![Build Status](https://travis-ci.com/alex4200/pytracov.svg?branch=master)](https://travis-ci.com/alex4200/pytracov)

[![codecov](https://codecov.io/gh/alex4200/pytracov/branch/master/graph/badge.svg)](https://codecov.io/gh/alex4200/pytracov)

[![contributors](https://github.com/alex4200/pytracov/graphs/contributors)]

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
I personally find the setup very complicated, as you have to login to each service, approve the access to github each, and add your repo - for each service in a different fashion. 

As I am no expert with these CI tools I created this example to see how it all works together. Unfortunately, there is not a single simple tool to do so. But with these tools you have a zillion features you probably never ever will use! 

## Repository setup
The repository contains example files for the setup of the tools. The relevant files are `.travis.yml`, `tox.ini` and `setup.py`. 

You can check the `tox` setup by running the command `tox -e py36` in the top level of the repo. It should run the tests and create a coverage report (which, for educational reasons, are not at 100%). 

## Service setup

### travis
To setup the *travis* service, you have to do the following:

1. Go to [travis-ci.com](travis-ci.com).
2. Log in with your *github* account.
3. Click on your profile picture.
4. On the Profile page the tab "Repositories" should be selected; then you click "Manage repositories on GitHub". You will be redirected to *github*.
5. On the github page you can approve access to either all your repositories, or you can select the one you want. 
6. Click on "Approve and install". 
7. You will be redirected back to *travis*, where your repository should appear in a list.
8. Click on your repository. It will probably not contain a lot.
9. But you can click on the badge on the top, where you casn copy-and-paste the "RESULT" URL to your Readme to show a badge of the build status. 
10. When you do a pull request, *travis* is activated, the test are being run, and the badge image is updated automatically. 


### codecov 
To setup the *codecov* service, you have to do the following:

1. Go to [codecov.io](codecov.io).
2. Log in with your *github* account.
3. Click on your *github* name.
4. Click on "Add new repository".
5. Here you should see your repositories. If not, click on the "Sync team repository list" on the bottom.
6. Select the repository to add. That's it. If you see the page with the title "Let's get your project covered." no further actions are required. It is a bit misleading.

## How it works
To see the setup in action, feel free to edit the file `editme.txt` and just edit something. If you are done, click "Create a new branch" at the buttom, and create a new pull request. 
This should trigger a build with the badges updated. 

You can also edit the file `tests/test_module2.py` and remove the comments and also create a new pull request. This time the coverage should increase!
