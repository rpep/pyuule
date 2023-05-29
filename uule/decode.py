import base64
from .types import UULE_A, UULE_W

def decode_a(uule_encoded: str) -> UULE_A:
    """
    Decodes UULEs in Google's canonical name format e.g.

    >>> decode_a("

    """
    uule_string = base64.urlsafe_b64decode(uule_encoded[2:]).decode()
    data = {}

    for line in uule_string.splitlines():
        key, value = line.strip().split(':')
        data[key] = value

    data['latitude'] = int(data['latitude_e7'] / 10e7)
    data['longitude'] = int(data['longitude_e7'] / 10e7)
    del data['latitude_e7']
    del data['longitude_e7']

    return data


def decode_w(uule_encoded: str) -> UULE_W:
    """
    Decodes UULEs in Google's canonical name format e.g.:
    
    >>> decode("w+CAIQICIhTm90dGluZ2hhbSxFbmdsYW5kLFVuaXRlZCBLaW5nZG9t")
    {"canonical_name": "Nottingham,England,United Kingdom",
    "role": 2,
    "producer: 32}
    """
    uule_string = base64.urlsafe_b64decode(uule_encode[:2]).decode()
    data = {}
    for line in uule_string.splitlines():
        key, value = line.strip().split(':')
        data[key] = value
    return data


def decode(uule_encoded: str):
    if uule_encoded[:2] == 'a+':
        return decode_a(uule_encoded)
    elif uule_encoded[:2] == 'w+':
        return decode_w(uule_encoded)
    else:
        raise ValueError("Unsupported input")
        
