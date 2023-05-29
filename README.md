# uule

UULE's are Google's objects for referencing locations. This Python library allows you to encode and encode UULE's!

There are two forms of UULE. The first type, prefixed by a 'w+':
```
w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t
```
can be used to direct searches to a specific location. The location must be drawn from Google's [list of canonical place names](https://developers.google.com/google-ads/api/data/geotargets"). A search can then be done with results drawn from the area around this location with a UULE query parameter added, for e.g.: [www.google.com?q=restaurants&uule=w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t](www.google.com?q=restaurants&uule=w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t)

This library allows you to encode and encode UULE's in this format:

```python3
import uule

uule.decode("w+CAIQICImV2VzdCBOZXcgWW9yayxOZXcgSmVyc2V5LFVuaXRlZCBTdGF0ZXM")
```


