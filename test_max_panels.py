from max_panels import max_paneles

def test_max_paneles():
    assert max_paneles(1, 2, 2, 4) == 4
    assert max_paneles(1, 2, 3 ,5) == 7
    assert max_paneles(2, 2, 1, 10) == 0

def test_orientaciones():
    assert max_paneles(3, 2, 6, 4) == 4
    assert max_paneles(3, 2, 6, 4) == max_paneles(2, 3, 6, 4)
    assert max_paneles(3, 2, 6, 4) == max_paneles(3, 2, 4, 6)
