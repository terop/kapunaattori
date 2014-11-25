#!/usr/bin/env python3

from __future__ import print_function
import os
from random import choice
import sys

from wordcache import WordCache


# The directory that contains this script file
THIS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
CACHE_DIRECTORY = "{}/cache".format(THIS_DIRECTORY)
WORDLIST_DIRECTORY = "{}/".format(THIS_DIRECTORY)

cache = WordCache(CACHE_DIRECTORY, WORDLIST_DIRECTORY)

