"""Happy-path tests for greet()."""

from greeter import greet


def test_greet_returns_hello_with_name():
    assert greet("Ada") == "Hi, Ada!"


def test_greet_uses_the_given_name():
    assert greet("Grace") == "Hello, Grace!"
