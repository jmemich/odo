from into.into import into

def test_into_convert():
    assert into(list, (1, 2, 3)) == [1, 2, 3]


def test_into_append():
    L = []
    result = into(L, (1, 2, 3))
    assert result == [1, 2, 3]
    assert result is L


def test_into_curry():
    assert callable(into(list))
    data = (1, 2, 3)
    assert into(list)(data) == into(list, data)
