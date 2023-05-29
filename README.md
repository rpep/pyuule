# uule

UULE's are Google's objects for referencing locations. This Python library allows you to encode and encode UULE's!

## What is a UULE anyway?

There are two forms of UULE. The first type, prefixed by a 'w+':
```
w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t
```
can be used to direct searches to a specific location. The location must be drawn from Google's [list of canonical place names](https://developers.google.com/google-ads/api/data/geotargets"). A search on Google can then be done with results drawn from the area around this location with a UULE query parameter added, for e.g.:
[www.google.com/search?q=restaurants&uule=w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t](http://www.google.com/search?q=restaurants&uule=w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t)


## Usage

This library allows you to encode and decode query parameter UULE's:

```python3
>>> import pyuule

>>> pyuule.decode_w("w+CAIQICImV2VzdCBOZXcgWW9yayxOZXcgSmVyc2V5LFVuaXRlZCBTdGF0ZXM")
"Nottingham,England,United Kingdom"

>>> pyuule.encode_w("Saint-Germain-des-Pres,Ile-de-France,France")
"w+CAIQICIrU2FpbnQtR2VybWFpbi1kZXMtUHJlcyxJbGUtZGUtRnJhbmNlLEZyYW5jZQ"
```

and additionaly allows you to decode cookie UULEs:

```
>>> pyuule.decode_a("a+cm9sZToxCnByb2R1Y2VyOjEyCnByb3ZlbmFuY2U6MAp0aW1lc3RhbXA6MTY4MDg3NzkwNjIzNjczNgpsYXRsbmd7CmxhdGl0dWRlX2U3OjMwMjY2NjY2MApsb25naXR1ZGVfZTc6LTk3NzMzMzMwMAp9CnJhZGl1czotMQo")
{
    "role": 1,
    "producer": 12,
    "provenance": 0,
    "timestamp": 1680877906236736,
    "latitude": 3.0266666,
    "longitude": -9.77333300,
    "radius": -1,
}
```


## Acknowledgements

The following blog post was helpful in writing this library:
https://valentin.app/uule.html
