from unittest import mock
from .mock import *
from strava_recommender.strava_client import Strava_Client



#@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="data")
#@mock.patch('json.load', return_value=mock_secret)
@mock.patch('requests.post', side_effect=mocked_requests)
class Test_Strava_Client:
    @mock.patch('requests.get', return_value=200)
    def test_no_oauth_get(self, mock_post, mock_get):
        """
        Testing mocked API get request without using OAuth.
        """
        client = Strava_Client('test_path', test=True)

        data = {
            'bounds': '-43.941875,172.322636,-43.451387,173.301242',
            'activity_type': 'running'
        }
        assert client.get('https://www.strava.com/api/v3/segments/explore', params=data) == 200



    @mock.patch('requests_oauthlib.OAuth2Session.fetch_token', return_value={'access_token': 'abc', 'refresh_token': 'abc'})
    @mock.patch('requests_oauthlib.OAuth2Session.get', side_effect=mocked_requests)
    def test_oauth_get(self, mock_post, mock_fetch, mock_get):
        """
        Testing mocked API get requests using OAuth.
        """
        client = Strava_Client('test_path', test=True)

        client.OAuth()

        client.authorize('http://localhost/?state=1UR5WX5e5p7LzCq5GgS4o8sLI74RX6&code=a1cecab69447fd4e3b5775e7698d15868e676678&scope=read,activity:read_all')

        client.get("https://www.strava.com/api/v3/athlete/activities")







