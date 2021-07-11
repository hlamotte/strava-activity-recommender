from .strava_client import Strava_Client
from .utils import polyline_to_latlong
import numpy as np


class Segment_Client(Strava_Client):
    def get_segments(self, sw_coords, ne_coords, activity_type):
        """
        Get Strava Segments within a rectangle.

        Args:
            ssw_coords ([list]): Coordinates [latitude, longitude] marking south-west edge of rectangle.
            ne_coords ([list]): Coordinates [latitude, longitude] marking north-east edge of rectangle.
            activity_type (string): 'running' or 'riding'.

        Raises:
            Exception: South-west coordinate is not south-west of north-east coordinate.

        Returns:
            list: List of segments.
        """
        #TODO: validating coordinates
        if np.all(sw_coords > ne_coords):
            raise Exception(f'Coordinate {sw_coords} is not south west of coordinate {ne_coords}.')
        explore_url = 'https://www.strava.com/api/v3/segments/explore'
        coords = [str(num) for num in sw_coords + ne_coords]
        bounds = ','.join(coords)
        params = {
            'bounds': bounds,
            'activity_type': activity_type,
            #'min_cat': ,
            #'max_cat': 
        }
        segments = self.get(explore_url, params=params).json()

        segments = self.prepare_segments(segments)

        return segments['segments']

    @staticmethod
    def prepare_segments(segments):
        """
        Pre-process segments.
    
        Convert Google Polylines to latlong lists.

        Args:
            segments (list): List of segments.

        Returns:
            segments: List of segments.
        """
        
        for segment_i, segment in enumerate(segments['segments']):
            segments['segments'][segment_i]['points'] = polyline_to_latlong(segment['points'])

        return segments
