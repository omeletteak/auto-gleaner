from privatter_fanbox_companion.platform import APP_NAME, default_data_dir


def test_default_data_dir_ends_with_app_name() -> None:
    assert default_data_dir().name == APP_NAME
