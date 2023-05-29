from dataclasses import dataclass

@dataclass
class UULE_LatLng:
    latitude_e7: int
    longitude_e7: int

@dataclass
class UULE_A:
    latitude: float
    longitude: float
    role: int
    provenance: int
    timestamp: int
    latlng: UULE_LatLng
    radius: int

@dataclass
class UULE_W:
    canonical_name: str
    producer: int
    role: int
