"""Tiny greeting helper for the GitHub Actions teaching lab."""


def greet(name: str, shout: bool = False) -> str:
    """Return a greeting for ``name``.

    When ``shout`` is true, the greeting is uppercase.
    """
    greeting = f"Hello, {name}!"
    if shout:
        return greeting.upper()
    return greeting
