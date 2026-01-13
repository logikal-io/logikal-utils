from logikal_utils.string import compact

def test_string() -> None:
    text = """hello
            world"""
    print(compact(text))
    assert compact(text) == 'hello world'