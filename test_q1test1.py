import q1test1

def test_compute():
    from math import cos,sinh,atan2
    fun = q1test1.compose(cos,sinh,atan2)
    assert fun(0.42, 3) == cos(sinh(atan2(0.42, 3)))