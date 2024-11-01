# ruff: noqa

from main import align


def test_align():
    poorly_aligned_string = """| Action| Command|
| -------| -------|
| Hello | `World` |
| This | `is an example` |
| of terrible | `alignment` |"""

    expected_output = """| Action      | Command         |
| -------     | -------         |
| Hello       | `World`         |
| This        | `is an example` |
| of terrible | `alignment`     |"""

    assert align("|", poorly_aligned_string) == expected_output
