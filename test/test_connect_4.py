from connect_4.connect_4 import say_hello


def test_say_hello() -> None:
    """Test the saludation. You can delete this."""
    assert say_hello("Alice") == "hello Alice!"
