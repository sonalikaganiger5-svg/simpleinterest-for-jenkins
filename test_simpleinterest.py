from simpleint import simint

def test_simpleint_pos():
    assert simint(2000,8,12) == 19200

def test_simpleint_zer():
    assert simint(10000,7,0) == 0

def test_simpleint_neg():
    assert simint(85000,-8,12) == -8160000