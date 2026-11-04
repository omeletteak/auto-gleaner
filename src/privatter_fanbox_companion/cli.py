"""コマンドラインの入口。M0 では骨組みのみ。"""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pfc",
        description="Fanbox 投稿の .txt から Privatter+ の原寸画像を保存します。",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="ルートフォルダを走査して処理する")
    run.add_argument("root", type=Path, help="PixivFanboxDownloader の保存先フォルダ")
    run.add_argument("--dry-run", action="store_true", help="抽出結果と保存予定パスを表示するだけ")
    run.add_argument("--verbose", "-v", action="store_true", help="詳細ログを表示する")
    run.add_argument("--config", type=Path, help="config.toml のパス")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "run":
        print("run はまだ実装されていません（M1 で実装予定）。")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
