from unittest import mock

import pytest

from xlgui.guiutil import ui_path

MOCK_EXAILE_DIR = "/mock"


@pytest.mark.parametrize(
    "path,expected_path",
    [
        (["a.py", ], f"{MOCK_EXAILE_DIR}/a.py"),
        (["a", "b.py"], f"{MOCK_EXAILE_DIR}/a/b.py"),
        (["a", "b", "c.py"], f"{MOCK_EXAILE_DIR}/a/b/c.py"),
    ],
)
@mock.patch("os.path.exists", lambda x: True)
@mock.patch("xl.xdg.data_dirs", [MOCK_EXAILE_DIR])
def test_ui_path(path, expected_path):
    output_path = ui_path(*path)
    assert output_path == expected_path


@pytest.mark.parametrize(
    "path,kwargs,expected_path",
    [
        (["a.py", ], {"relto": "/"}, "/a.py"),
        (["a", "b.py"], {"relto": "/"}, "/a/b.py"),
        (["c.py", ], {"relto": "/a/b"}, "/a/c.py"),
        (["d.py", ], {"relto": "/a/b/c"}, "/a/b/d.py")
    ],
)
def test_ui_path_relative(path, kwargs, expected_path):
    output_path = ui_path(*path, **kwargs)
    assert output_path == expected_path


def test_ui_path_kwargs_other_then_realto():
    with pytest.raises(ValueError):
        ui_path([], a="b")
