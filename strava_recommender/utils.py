from pypolyline.util import decode_polyline
import numpy as np

def polyline_to_latlong(polyline):
    if polyline is None:
        return np.nan
    return decode_polyline(bytes(polyline, "utf-8"), 5)