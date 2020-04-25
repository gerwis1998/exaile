from unittest import mock

import pytest

from xl.common import open_file, clamp


@pytest.mark.parametrize(
    "platform,expected_arg",
    [
        ("darwin", "open"),
        ("linux", "xdg-open"),
    ]
)
def test_open_file_non_windows(platform, expected_arg):
    path = "/"
    with mock.patch("sys.platform", platform), mock.patch("subprocess.Popen") as mocked_popen:
        open_file(path)
        assert mocked_popen.called
        assert mocked_popen.call_args[0][0][0] == expected_arg
        assert mocked_popen.call_args[0][0][1] == path


@pytest.mark.parametrize(
    "value,minimum,maximum,expected",
    [
        (2, 1, 3, 2),   # normal example
        (-1, 1, 2, 1),  # value lower then minimum
        (3, 1, 2, 2),   # value higher then maximum
        (2, 3, 1, 3),   # minimum higher then maximum
        (1, 1, 1, 1),   # all values are the same
    ]
)
def test_clamp(value, minimum, maximum, expected):
    result = clamp(value, minimum, maximum)
    assert result == expected
