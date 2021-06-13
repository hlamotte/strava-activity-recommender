from strava_recommender import utils

def test_polyline_to_latlong():
    polyline  ='xi{hG_oz|_@LCb@DxAf@t@PbAHj@TXFdABbANbAD`@?p@QbAMf@O`@I`@?XKx@CZMbBSb@IJ@|@d@\\V\\H\\I`@EbAHt@LZ?XE^Dt@A^F|@X^GVKZ?b@G`@MZCPEb@Yb@a@VOJAv@@\\CXIf@I`@Mp@MNGTYl@kBLg@pAqAl@oATWf@c@n@Wd@[^a@Rw@Be@AaAJo@`@k@FO`EmFNKJOPa@Jk@Gc@Oc@C]Dm@FKJGz@Bh@In@SJGHQFQ@Q?iBF_@DKVU\\O^KPIHMTcBn@iARgA?k@BQDOHONEd@BRCP?h@Jv@OZMXSp@k@b@YX[\\WdVeDbC@h@HNHb@Lv@Ld@?P@~@G^Id@B^ARENAx@S`AAREvAFb@Cb@MH?z@Ll@DPFZ?JFL@XAj@Df@Bv@Z^ZPFd@Xr@l@h@XVBl@C^DTNLDXFb@Bj@Tj@ZLB\\BJBFHf@dAz@pATHf@AZL'
    lat_long = utils.polyline_to_latlong(polyline)
    assert type(lat_long) == list
    assert len(lat_long[0]) == 2