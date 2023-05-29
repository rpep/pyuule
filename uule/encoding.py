import base64
from datetime import datetime
from .types import UULE_A
import urllib

def pad(uule):
    """
    For base64 decoding, padding bytes need to be added. These are stripped out
    for UULE transmission.
    """
    return uule + '=' * (4 - len(uule) % 4)

def decode_a(uule) -> UULE_A:
    """
    Decodes UULE's of type "a+......"
    """
    uule = uule[2:]
    lines = base64.urlsafe_b64decode(pad(uule)).decode().split("\n")
    data = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':')
            data[key] = value
    data["latitude"] = float(data.pop("latitude_e7")) / 10e7
    data["longitude"] = float(data.pop("longitude_e7")) / 10e7
    data["radius"] = int(data["radius"])
    data["role"] = int(data["role"])
    data["producer"] = int(data["producer"])
    data["provenance"] = int(data["provenance"])
    data["radius"] = int(data["radius"])
    return data

def decode_w(uule) -> str:
    """
    Decodes UULE's of type "w+...."
    """
    uule = urllib.parse.unquote(uule[10:]).replace("-", "+").replace("_", "/")
    return base64.urlsafe_b64decode(pad(uule)).decode().lstrip()

def encode_w(canonical_location) -> str:
    """
    Canonical location must be from the list at 
    """
    ascii_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    len_bytes = ascii_map[len(canonical_location)]
    location = base64.urlsafe_b64encode(bytes(canonical_location, "ascii")).decode()
    return f"w+CAIQICI{len_bytes}{location}"