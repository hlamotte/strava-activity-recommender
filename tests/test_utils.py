from strava_recommender import utils
import numpy as np
import pytest
import os

@pytest.fixture(autouse=True, scope='session')
def cleanup_files():
    pass
    files = ['tests/fixtures/test.csv']
    yield
    for file in files:
        os.remove(file)

def test_polyline_to_latlong():
    polyline  ='xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL'
    lat_long = utils.polyline_to_latlong(polyline)
    assert type(lat_long) == list
    assert len(lat_long[0]) == 2
    lat_long = np.array(lat_long)
    assert np.all(np.logical_and(lat_long[:, 0] > -90, lat_long[:, 0] < 90))
    assert np.all(np.logical_and(lat_long[:, 1] > -180, lat_long[:, 1] < 180))

def test_save_json_list():
    segments = [
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True}
            ]
    test_file = 'tests/fixtures/test.csv'
    utils.save_json_list(segments, test_file)
    
    with open(test_file) as f:
        row_count = sum(1 for row in f)
    assert row_count == 4


    # empty segments response
    
    segments = []
    utils.save_json_list(segments, test_file)
    with open(test_file) as f:
        row_count = sum(1 for row in f)
    assert row_count == 4

    segments = [
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True},
                {'id': 1015892, 'resource_state': 2, 'name': 'Rapaki  bottom to top', 'climb_category': 2, 'climb_category_desc': '3', 'avg_grade': 7.7, 'start_latlng': [-43.562682140659135, 172.66432497666466], 'end_latlng': [-43.59441787008531, 172.67346041293132], 'elev_difference': 318.8, 'distance': 4128.3, 'points': 'xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL', 'starred': False, 'elevation_profile': 'https://d3o5xota0a1fcr.cloudfront.net/v6/charts/2KBJBJLOXRX4XJZHFIK5GCQ5FFRFVEVFUTNJJU5225EPTP4XA6LDDGIYPAQYXYA4FVXC3KMAJ7DMSG5HAEEA====', 'local_legend_enabled': True}
            ]

    utils.save_json_list(segments, test_file)
    with open(test_file) as f:
        row_count = sum(1 for row in f)
    assert row_count == 6
