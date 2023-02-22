import splosion as txt
def test_string_bits():
    assert txt.string_bits("hello") == 'hlo'
    assert txt.string_bits("hi") == 'h'
    assert txt.string_bits("heeololeo") == 'hello'