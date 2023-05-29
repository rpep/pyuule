from .types import UULE_A, UULE_W
from base64 import urlsafe_b64encode

def encode(latitude: float, longitude: float, radius: int =-1, role: int = 1, producer = 12, provenance=0, timestamp=None):
    lat_e7 = int(latitude * 10e7)
    lon_e7 = int(longitude * 10e7)
    uule_string = f"""\
      role:{role}
      producer:{producer}
      provenance:{provenance}
      timestamp:{!timestamp ? int(time.time() * 10e7) : timestamp}
      latlng{{
      latitude_e7:{int(latitude * 10e7)}
      longitude_e7:{int(longitude * 10e7)}
      }}
      radius:{radius}
    """

    uule_encoded = urlsafe_b64encode(uule_string.encode()).decode()
    return 'a+' + uule_encoded
