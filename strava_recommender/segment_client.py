from .strava_client import Strava_Client


class Segment_Client(Strava_Client):
    def get_segments(self, sw_coords, ne_coords, activity_type):
        #TODO: validating coordinates
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

        return segments

    @staticmethod
    def prepare_segments(self, segments):
        for segment in segments:
            print(segments)
