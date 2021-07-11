from pypolyline.util import decode_polyline
import numpy as np
import os
import csv

def polyline_to_latlong(polyline):
    """
    Convert Google Polyline to latlong list.

    Args:
        polyline (string): Google Polyline string.

    Returns:
        list: Latlong list.
    """
    if polyline is None:
        return np.nan

    # switch from lon, lat to lat, lon
    lon_lat = decode_polyline(bytes(polyline, "utf-8"), 5)
    lat_lon = [coord[::-1] for coord in lon_lat]
    return lat_lon

def save_json_list(json_list, filename):
    """
    Append json_list to csv file.

    Args:
        json_list ([type]): [description]
        filename ([type]): [description]
    """
    print(json_list)
    if len(json_list) > 0:
        # json_list exists in box
        file_exists = os.path.isfile(filename)
        
        with open(filename, 'a') as csvfile:
            fieldnames = json_list[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for segment in json_list:
                writer.writerow(segment)