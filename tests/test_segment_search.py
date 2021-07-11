from strava_recommender.segment_search import *
import numpy as np
import os
from unittest import mock
from .mock import *

def test_prepare_sub_rectangles():
    test_coords = (
        (-20, 30),
        (-10, 40)
    )
    bl_coords, br_coords, tl_coords, tr_coords = prepare_sub_rectangles(*test_coords)
    assert np.array_equal(bl_coords, ((-20, 30), (-15, 35)))
    assert np.array_equal(br_coords, ((-20, 35), (-15, 40)))
    assert np.array_equal(tl_coords, ((-15, 30), (-10, 35)))
    assert np.array_equal(tr_coords, ((-15, 35), (-10, 40)))


segments = [
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True}
            ]
@mock.patch('strava_recommender.segment_client.Segment_Client.get_segments', return_value=segments)
@mock.patch('requests.post', side_effect=mocked_requests)
def test_get_all_segments(mock_client, mock_post):
    filename = get_all_segments('test_path', 'tests/fixtures/', (10, 10), (11, 11), 'running', test=True)
    os.remove(filename)

    
