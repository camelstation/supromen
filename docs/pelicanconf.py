AUTHOR = 'camelstation'
SITENAME = 'supromen'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# We keep docs/index.html as a hand-written splash page.
# So: do not let Pelican generate any direct template pages (including index.html).
DIRECT_TEMPLATES = ()
PAGINATED_DIRECT_TEMPLATES = ()
INDEX_SAVE_AS = ""



# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
