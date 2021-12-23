"""
Works with mypy.
"""
from hamcrest.core import assert_that
from hamcrest.core.core import is_

def test() -> None:
    assert_that(1, is_(1))
