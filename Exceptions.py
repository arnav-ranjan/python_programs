class ValueTooHighError(Exception):
    pass

def test_Value(x):
    if x > 100:
        raise ValueTooHighError("value too high")
test_Value(200)