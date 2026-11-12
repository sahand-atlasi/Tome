import tome


def test_package_exposes_version() -> None:
    assert tome.__version__ == "0.0.1"
