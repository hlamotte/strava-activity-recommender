from strava_recommender.segment_client import Segment_Client
from .mock import *
from unittest import mock, TestCase
import numpy as np


@mock.patch('requests.post', side_effect=mocked_requests)
class Test_Segment_Client(TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests)
    def test_get_segments(self, mock_post, mock_get):

        client = Segment_Client('test_path', test=True)

        segments = client.get_segments((-43.592221, 172.726649), (-43.590974, 172.729756), 'running')

        # assert start and end latlong equal to decoded start and end
        assert np.allclose(np.array(segments[0]['start_latlng']), np.array(segments[0]['points'][0]))
        assert np.allclose(np.array(segments[0]['end_latlng']), np.array(segments[0]['points'][-1]))

        with self.assertRaises(Exception) as context:
            client.get_segments((-43.590974, 172.729756), (-43.592221, 172.726649), 'running')

    def test_prepare_segments(self, mock_post):
        test_segments = {
            'segments': [
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True}
            ]
        }
        prepared_segments = Segment_Client.prepare_segments(test_segments)
        assert len(prepared_segments['segments']) == 3

        # assert start and end latlong equal to decoded start and end
        assert np.allclose(np.array(prepared_segments['segments'][0]['start_latlng']), np.array(prepared_segments['segments'][0]['points'][0]))
        assert np.allclose(np.array(prepared_segments['segments'][0]['end_latlng']), np.array(prepared_segments['segments'][0]['points'][-1]))



