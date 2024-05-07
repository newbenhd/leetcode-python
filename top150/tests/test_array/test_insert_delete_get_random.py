from top150.array_ import RandomizedSet


def test_randomized_set():
    randomSet = RandomizedSet()
    assert randomSet.insert(1)
    assert not randomSet.remove(2)
    assert randomSet.insert(2)
    assert randomSet.getRandom() in [1, 2]
    assert randomSet.remove(1)
    assert not randomSet.insert(2)
    assert randomSet.getRandom() == 2
