# pylint: disable=missing-function-docstring

from main import pad_cell


def test_align():
    assert pad_cell('Hello', 0) == 'Hello'
    assert pad_cell('Hello', 5) == 'Hello'
    assert pad_cell('Hello', 6) == 'Hello '
    assert pad_cell('Hello', 7) == 'Hello  '
    assert pad_cell('Hello', 9) == 'Hello    '
