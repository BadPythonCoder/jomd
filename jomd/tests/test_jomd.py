from jomd import __version__
from jomd import screen


def test_version():
    assert __version__ == '0.1.0'

window = screen.Window("test", (200, 200))