"""
Fails mypy with

example_import_from_base.py:7: error: Module "hamcrest" does not explicitly export attribute "assert_that"; implicit reexport disabled
example_import_from_base.py:7: error: Module "hamcrest" does not explicitly export attribute "is_"; implicit reexport disabled
"""
from hamcrest import assert_that, is_

def test() -> None:
    assert_that(1, is_(1))
