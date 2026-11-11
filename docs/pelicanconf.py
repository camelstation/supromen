import os

AUTHOR = 'camelstation'
SITENAME = 'supromen'
SITEURL = ""

PATH = "content"

# Build-time list of About page slideshow images, read from
# content/images/about/. Sorted numerically by filename so 2.webp sorts
# before 10.webp. Adding/removing files there and rebuilding is all
# that's needed to update the slideshow -- no template/JS changes required.
def _about_slideshow_sort_key(filename):
    stem = os.path.splitext(filename)[0]
    if stem.isdigit():
        return (0, int(stem), stem)
    return (1, 0, stem)

_about_images_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "content", "images", "about"
)

if os.path.isdir(_about_images_dir):
    ABOUT_SLIDESHOW_IMAGES = [
        "/images/about/" + filename
        for filename in sorted(
            os.listdir(_about_images_dir), key=_about_slideshow_sort_key
        )
        if not filename.startswith(".")
    ]
else:
    ABOUT_SLIDESHOW_IMAGES = []

# Same as above, for the Studio for rent page slideshow
# (content/images/studio-for-rent/).
_studio_for_rent_images_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "content", "images", "studio-for-rent"
)

if os.path.isdir(_studio_for_rent_images_dir):
    STUDIO_FOR_RENT_SLIDESHOW_IMAGES = [
        "/images/studio-for-rent/" + filename
        for filename in sorted(
            os.listdir(_studio_for_rent_images_dir), key=_about_slideshow_sort_key
        )
        if not filename.startswith(".")
    ]
else:
    STUDIO_FOR_RENT_SLIDESHOW_IMAGES = []
PAGE_PATHS = ["pages", "shop"]
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

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

# Use our minimal theme
THEME = "theme"
# Serve theme assets from /assets/ instead of /theme/ to avoid “copy onto itself” issue
THEME_STATIC_DIR = "assets"

# Copy static images from content/images -> output/images
STATIC_PATHS = ["images", "redirects"]

# Redirect pages for old URLs (pages were renamed). Copied as-is to the old
# addresses so existing links/bookmarks still work, #anchors included.
EXTRA_PATH_METADATA = {
    "redirects/events.html": {"save_as": "events/index.html"},
    "redirects/upcoming.html": {"save_as": "upcoming/index.html"},
}
# Don't let Pelican try to read the redirect pages as articles.
ARTICLE_EXCLUDES = ["redirects"]

# Keep docs/index.html as a hand-written splash page (not Pelican-generated)
DIRECT_TEMPLATES = ()
INDEX_SAVE_AS = ""



# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
