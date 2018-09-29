from encode import encode

def test_empty_string():
    assert encode("") == ""

def test_non_repeat():
    assert encode("a") == "a"

def test_solution():
    assert encode("aabcccccaaa") == "a2b1c5a3"

def test_fringe():
    assert encode("abc") == "a1b1c1"
    assert encode("aabbaa") == "a2b2a2"