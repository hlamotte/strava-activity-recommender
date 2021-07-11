"""Exhaustively get all the Strava segments in a rectangular area."""
from .segment_client import Segment_Client
from datetime import datetime
import numpy as np
from .utils import save_json_list

def get_all_segments(credentials_path, output_prefix, sw_coords, ne_coords, activity_type, test=False):
    """
    Get all Strava Segments exhaustively from a rectangle and save to csv file.

    Retains duplicate segments.

    Args:
        credentials_path (string): Path to json file containing Strava API credentials.
        output_prefix (string): Path to folder where to save resulting csv containing segments.
        sw_coords ([list]): Coordinates [latitude, longitude] marking south-west edge of rectangle.
        ne_coords ([list]): Coordinates [latitude, longitude] marking north-east edge of rectangle.
        activity_type (string): 'running' or 'riding'.
        test (bool, optional): Hits mock API for tests when set to True. Defaults to False.

    Returns:
        string: Filename of file resulting csv containing segments.
    """
    client = Segment_Client(credentials_path, test=test)
    filename = output_prefix + 'segments_'  + activity_type + '_' + datetime.now().isoformat() + '_' + '|'.join(map(str, sw_coords)) + '_' + '|'.join(map(str, ne_coords)) +  '.csv'
    #print(filename)
    get_segments(client, sw_coords, ne_coords, activity_type, filename)

    return filename


def get_segments(client, sw_coords, ne_coords, activity_type, filename):
    """
    Get Segments in rectangle.

    Recurse on sub-rectangle if returns ten Segments.

    Args:
        client (Strava_Client): Instance of Strava_Client class. Does not need to be OAuth authenticated.
        sw_coords ([list]): Coordinates [latitude, longitude] marking south-west edge of rectangle.
        ne_coords ([list]): Coordinates [latitude, longitude] marking north-east edge of rectangle.
        activity_type (string): 'running' or 'riding'.
        filename (string): Filename of resulting csv for saving segments.
    """
    segments = client.get_segments(sw_coords, ne_coords, activity_type)
    
    # need to handle failures here, or in the client?
    save_json_list(segments, filename)
    # append data to file here

    if len(segments) == 10:

        bl_coords, br_coords, tl_coords, tr_coords = prepare_sub_rectangles(sw_coords, ne_coords)

        # recurse on four sub-rectangles
        # bottom-left rectangle

        get_segments(client, *bl_coords, activity_type, filename)
        # bottom-right rectangle
        get_segments(client, *br_coords, activity_type, filename)
        # top-left rectangle

        get_segments(client, *tl_coords, activity_type, filename)
        # top-right rectangle
        get_segments(client, *tr_coords, activity_type, filename)


def prepare_sub_rectangles(sw_coords, ne_coords):
    """
    Prepare coordinates for four sub-rectangles splitting original rectangle in half along longitudinal and latitudinal axis.

    Args:
        sw_coords ([list]): Coordinates [latitude, longitude] marking south-west edge of rectangle.
        ne_coords ([list]): Coordinates [latitude, longitude] marking north-east edge of rectangle.
    """
    original_coords = np.array([sw_coords, ne_coords])

    mid_lat = np.mean(original_coords[:,0])
    mid_lon = np.mean(original_coords[:,1])

    bl_coords = (sw_coords, (mid_lat, mid_lon))
    br_coords = ((sw_coords[0], mid_lon), (mid_lat, ne_coords[1]))
    tl_coords = ((mid_lat, sw_coords[1]), (ne_coords[0], mid_lon))
    tr_coords = ((mid_lat, mid_lon), ne_coords)

    return bl_coords, br_coords, tl_coords, tr_coords
