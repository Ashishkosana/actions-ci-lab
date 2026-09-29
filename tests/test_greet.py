"""Tests for greet()."""

from greeter import greet


def test_greet_returns_hello_with_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_uses_the_given_name():
    assert greet("Grace") == "Hello, Grace!"


def test_greet_shout_uppercases_the_greeting():
    assert greet("Ada", shout=True) == "HELLO, ADA!"


def test_greet_shout_uses_the_given_name():
    assert greet("Grace", shout=True) == "HELLO, GRACE!"
