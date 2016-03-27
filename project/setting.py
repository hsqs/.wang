# -*- encoding:utf-8 -*-

import os


REPO_NAME = ''  # used for freezer_base_url
DEBUG = True


# Assumes the app is located in the same directory
APP_DIR = os.path.dirname(os.path.abspath(__file__))


def parent_dir(path):
    ''' return the parent of a directory
    Args:
        path: a file path
    '''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)

# a configuration to put static pages to the project root
FREEZER_DESTINATION = PROJECT_ROOT

# since it is a repo page, not a Github user page, we need to
# set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
# important:if this is True, all app files will be deleted when you run freezer
FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = ".md"

# set to True, Frozen-Flask won’t show warnings if the MIME type returned from the
# server doesn’t match the MIME type derived from the filename extension
FREEZER_IGNORE_MIMETYPE_WARNINGS = True
