### CDN Support

*pelican plugin*

This plugin will replace  the url of `CDN_TYPE` resource with your cdn url.


SETTINGS:

`pelicanconf.py`
```
PLUGIN_PATHS = ['...']
PLUGINS = ['cdn_support']
```



`publishconf.py`
```
CDN_TYPE = [".css", ".js", ".jpeg", ".png", ".gif", ".jpg"]
CDN_DOMAIN = "your.cdn.domain"
```



