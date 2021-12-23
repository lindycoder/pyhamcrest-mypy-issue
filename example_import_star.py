"""
Fails mypy with

example_import_star.py:10: error: Name "assert_that" is not defined
example_import_star.py:10: error: Name "is_" is not defined
"""
from hamcrest import *

def test() -> None:
    assert_that(1, is_(1))
