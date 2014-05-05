#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gauteng Python User Group'
SITENAME = u'gautengpug'
SITEURL = ''

TIMEZONE = 'Africa/Johannesburg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('This page', 'http://gautengpug.github.io/'),
          ('Google Group', 'https://groups.google.com/forum/#!forum/gpugsa'),
          ('Meetup link coming soon', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/gautengpug'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'

#settings for the site itself
DISPLAY_CATEGORIES_ON_MENU = True
SHOW_ARTICLE_CATEGORY = True
PYGMENTS_STYLE = 'emacs'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_TAGS_ON_SIDEBAR = True