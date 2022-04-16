class ValueTooHighError(Exception):
    pass

def test_Value(x):
    if x > 100:
        raise ValueTooHighError("value too high")

try:
    test_Value(200)
except ValueTooHighError as e:
    print(e)