"""OS 固有の処理はすべてこのモジュールに集める。

他のモジュールは sys.platform や os.name を直接見ないこと。
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

APP_NAME = "auto-gleaner"


def is_windows() -> bool:
    return sys.platform == "win32"


def default_data_dir() -> Path:
    """ログや状態ファイルの既定の置き場所。"""
    if is_windows():
        base = os.environ.get("LOCALAPPDATA")
        root = Path(base) if base else Path.home() / "AppData" / "Local"
    else:
        base = os.environ.get("XDG_STATE_HOME")
        root = Path(base) if base else Path.home() / ".local" / "state"
    return root / APP_NAME
