
mock_secret = {
    "client_id": 1,
    "client_secret": "abc",
    "refresh_token": "abc"
}

def mocked_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://www.strava.com/api/v3/segments/explore':
        response = {
            'segments': [
                {'id': 1015892,
                'resource_state': 2,
                'name': 'Rapaki  bottom to top',
                'climb_category': 2,
                'climb_category_desc': '3',
                'avg_grade': 7.7,
                'start_latlng': [-43.562682140659135, 172.66432497666466],
                'end_latlng': [-43.59441787008531, 172.67346041293132],
                'elev_difference': 318.8,
                'distance': 4128.3,
                'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL',
                'starred': False,
                'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====',
                'local_legend_enabled': True}
            ]
        }
        return MockResponse(response, 200)
    elif args[0][:35] == 'https://www.strava.com/oauth/token?':
        response = {
            'access_token': 'abc',
            'refresh_token': 'abc'
        }
        return MockResponse(response, 200)

    elif args == "https://www.strava.com/api/v3/athlete/activities":
        response = {
            'nonsense': 'nonsense'
        }
        return MockResponse(response, 200)


    return MockResponse(None, 404)