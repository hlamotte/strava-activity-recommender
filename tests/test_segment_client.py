from .test_strava_client import Test_Strava_Client
from strava_recommender.segment_client import Segment_Client
from .mock import *
from unittest import mock

@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
@mock.patch('json.load', return_value=mock_secret)
@mock.patch('requests.post', side_effect=mocked_requests)
class Test_Segment_Client():
    @mock.patch('requests.get', side_effect=mocked_requests)
    def test_get_segments(self, mock_open, mock_load, mock_post, mock_get):

        client = Segment_Client('.credentials_path.json')

        segments = client.get_segments([37.8331119, -122.4834356], [37.8280722, -122.4981393], 'running')

        print(segments)

        assert 1==2

    #def test_prepare_segments(self):


