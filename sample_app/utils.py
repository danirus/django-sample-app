#-*- coding: utf-8 -*-
# Use this function to break django-sample-project unittests.
# If the function returns an integer tests will pass, but if the function
# returns a string the tests of django-sample-project will fail.
#
# This is part of the buildbdot-sample-conf continuous integration story:
#  https://github.com/danirus/buildbot-sample-conf
#  https://github.com/danirus/django-sample-project

def do_something():
    "Use this function to break django-sample-project tests"
    return 10
