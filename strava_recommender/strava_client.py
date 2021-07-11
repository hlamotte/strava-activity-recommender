from requests_oauthlib import OAuth2Session
import urllib.parse as urlparse
from urllib.parse import parse_qs
import json
import requests


#TODO: protect accessing credentials with private attributes


class Strava_Client():
    '''
    Strava client.

    Can make post requests not requiring OAuth after successful instantiation. 
    
    To make post requests requiring OAuth call the OAuth() method, and after authenticating in a browser
    paste the resulting url into the authorize(url) method.

    Args:
        credentials_path (str): Path to a json file containing your client_id, client_secret and refresh token
        test (bool, optional): Hits mock API for tests when set to True. Defaults to False.

    '''
    def __init__(self, credentials_path, test=False):
        
        # read credentials from strava_credentials.json
        self.credentials_path = credentials_path
        if test:
            self.credentials_path = 'tests/fixtures/test_credentials.json'
        
        self.read_credentials()

        self.update_token()

        self.oauth = None

    def update_token(self):
        '''Update access and refresh tokens'''
        # make POST request to Strava API
        req = requests.post("https://www.strava.com/oauth/token?client_id={}&client_secret={}&refresh_token={}&grant_type=refresh_token".format(self.client_id, self.client_secret, self.refresh_token)).json()
        #print(req)
        # get credentials
        self.access_token = req['access_token']
        self.refresh_token = req['refresh_token']
    
    def read_credentials(self):
        '''Read credentials from credentials file'''
        # read credentials from strava_credentials.json
        with open(self.credentials_path, 'r') as f:
            api_credentials = json.load(f)
        
        self.client_id = api_credentials['client_id']
        self.client_secret = api_credentials['client_secret']
        self.refresh_token = api_credentials['refresh_token']

        
    def OAuth(self):
        '''Authenticate session using OAuth'''
        self.update_token()
        self.oauth = OAuth2Session(self.client_id, scope='activity:read_all', redirect_uri='http://localhost')

        params = {
            "client_secret" : self.client_secret,
            "code" : self.access_token,
        }

        #https://www.strava.com/oauth/authorize?client_id=your_client_id&redirect_uri=http://localhost&response_type=code&scope=activity:read_all

        authorization_url, state = self.oauth.authorization_url(
            'https://www.strava.com/oauth/authorize?',
            **params)
        print('Please go to the following url and authorize access, and copy resulting url: \n',authorization_url)
    
    
    def authorize(self, authorization_url):
        '''Provide the OAuth authentication resulting url'''



        #http://localhost/?state=1UR5WX5e5p7LzCq5GgS4o8sLI74RX6&code=a1cecab69447fd4e3b5775e7698d15868e676678&scope=read,activity:read_all


        parsed = urlparse.urlparse(authorization_url)
        auth_code = parse_qs(parsed.query)['code'][0]

        #https://www.strava.com/oauth/token?client_id=66592&client_secret=cf4a14cf4b1861474c436758ef5e5614f9e9712c&code=7640147de7c7b5092674333a8943fd73cf363bc9&grant_type=authorization_code


        res = self.oauth.fetch_token(
                'https://www.strava.com/oauth/token?',
                code=auth_code,
                include_client_id=True,
                client_secret=self.client_secret)
        # update credentials
        self.access_token = res['access_token']
        self.refresh_token = res['refresh_token']
        
    
    def get(self, url, params={}):
        '''Make get request to the Strava API'''

        self.update_token()

        headers = {"Authorization": f"Bearer {self.access_token}"}
        if self.oauth is not None:
            return self.oauth.get(url, params=params)
        return requests.get(url, params=params, headers=headers)



    
