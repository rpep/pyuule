import pyuule
import pytest


@pytest.mark.parametrize(
    "uule,location",
    [
        (
            "w+CAIQICIrU2FpbnQtR2VybWFpbi1kZXMtUHJlcyxJbGUtZGUtRnJhbmNlLEZyYW5jZQ",
            "Saint-Germain-des-Pres,Ile-de-France,France",
        )
    ],
)
def test_query_param_uule_methods(uule, location):
    # Test the decoding methods
    decoded = pyuule.decode_w(uule)
    assert decoded == location
    # And then test the other direction
    assert pyuule.encode_w(location) == uule


@pytest.mark.parametrize(
    "uule,decoded",
    [
        (
            "a+cm9sZToxCnByb2R1Y2VyOjEyCnByb3ZlbmFuY2U6MAp0aW1lc3RhbXA6MTY4MDg3NzkwNjIzNjczNgpsYXRsbmd7CmxhdGl0dWRlX2U3OjMwMjY2NjY2MApsb25naXR1ZGVfZTc6LTk3NzMzMzMwMAp9CnJhZGl1czotMQo",
            {
                "role": 1,
                "producer": 12,
                "provenance": 0,
                "timestamp": 1680877906236736,
                "latitude": 3.0266666,
                "longitude": -9.77333300,
                "radius": -1,
            },
        ),
        (
            "a+cm9sZToxCnByb2R1Y2VyOjEyCnByb3ZlbmFuY2U6Ngp0aW1lc3RhbXA6MTU5MTUyMTI0OTAzNDAwMApsYXRsbmd7CmxhdGl0dWRlX2U3OjM3NDIxMDAwMApsb25naXR1ZGVfZTc6LTEyMjA4NDAwMDAKfQpyYWRpdXM6OTMwMDA%3D",
            {
                "role": 1,
                "producer": 12,
                "provenance": 6,
                "timestamp": 1591521249034000,
                "latitude": 3.7421,
                "longitude": -12.2084,
                "radius": 93000,
            },
        ),
    ],
)
def test_decode_a(uule, decoded):
    assert decoded == pyuule.decode_a(uule)
