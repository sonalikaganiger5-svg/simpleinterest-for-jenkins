from simpleint import simint

def test_simpleint_pos():
    assert simint(2000,8,12) == 1920

def test_simpleint_zer():
    assert simint(10000,7,0) == 0
