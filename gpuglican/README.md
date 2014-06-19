# gpuglican

This is a theme for [Pelican](https://pelican.readthedocs.org), created for the
[GPUG](https://gautengpug.github.io/) site. It is basically the excellent
[pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) theme with
a few small alterations. Please see pelican-bootstrap3's documentation for more
information.


## Installation

Point the `THEME` variable in your `pelicanconf.py` to `/path/to/gpuglican`

## Usage

Beyond Pelican settings and features supported by
[pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3), this
theme adds the following features:

### Show an announcement on the home page

Setting `SHOW_ANNOUNCEMENT_ON_HOME` to `True` will search for the *first*
*article* with an `announcement_text` attribute set. The value of this
attribute, prefixed by the optional `ANNOUNCEMENT_PREFIX` setting, is displayed
in a [Bootstrap alert](http://getbootstrap.com/components/#alerts) on the home
page (only).

For GPUG's usage the article announcing a meetup is given an
`announcement_text` attribute with the value being the date of the meetup, and
`ANNOUNCEMENT_PREFIX` is set to "NEXT MEETUP: ". This means announcements will
be of the format "NEXT MEETUP: 1 January 1970".

### Embedding pages in the home page

If the `EMBED_PAGES_IN_HOME` setting is set to `True`, all *pages* with a
truthy `embed_in_homepage` attribute will be embedded in the home page
(`index.html`), *before* the articles list.

By default, only the page's content is embedded. If you would like to include
the titles of these pages, set the `EMBED_PAGES_TITLES_IN_HOME` setting to
`True`.
