# auto-gleaner

[PixivFanboxDownloader](https://github.com/xuejianxianzun/PixivFanboxDownloader) で保存した Fanbox 投稿フォルダを後処理するローカル CLI です。
投稿本文の `.txt` に書かれた Privatter+（`https://privatter.me/page/...`）の URL とパスワードを読み取り、ページの原寸画像を `.txt` と同じフォルダに保存します。

PixivFanboxDownloader 本体には手を入れない、独立したツールです。

> 開発中です。現在は M0（雛形）の段階で、`run` はまだ動きません。

## 必要なもの

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)
- Windows 11（後で Linux / ARM にも対応予定）

## セットアップ

```powershell
git clone <このリポジトリ>
cd auto-gleaner
uv sync --locked   # uv.lock と一致しない場合は失敗する
```

## 使い方（予定）

```powershell
uv run auto-gleaner run "C:\path\to\fanbox" --dry-run   # 抽出結果の確認のみ
uv run auto-gleaner run "C:\path\to\fanbox"             # 本処理
uv run auto-gleaner run "C:\path\to\fanbox" --verbose   # 詳細ログ
```

設定は `config.example.toml` を `config.toml` にコピーして編集します。

## 開発

```powershell
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

- OS 固有の処理は `src/auto_gleaner/platform.py` にだけ書く。パスはすべて `pathlib`。
- 実データ（txt、HTML、cookies、パスワード）はコミットしない。`tests/fixtures/` には匿名化したものだけを置く。

## 依存パッケージの方針（サプライチェーン対策）

- 実行時の依存は最小限にする。標準ライブラリで足りるものは標準ライブラリを使う（現在、実行時の依存はゼロ）
- 追加するのは、広く使われていて保守が続いている有名なパッケージだけにする。追加前に PyPI で正確な名前、配布元、リポジトリを確認する（綴りの似た偽パッケージに注意）
- `uv.lock` をコミットし、全パッケージをバージョンと sha256 ハッシュで固定する。インストールは `uv sync --locked` で行う
- `pyproject.toml` の `exclude-newer = "7 days"` で、公開から7日たっていない版は使わない（乗っ取りで公開された悪性版を避けるため）
- 依存を足すときは、何が推移的に入るかを `uv tree` で確認する
- ネイティブコードを含むパッケージや、利用者の少ないパッケージ（例: ブラウザ Cookie を読む rookiepy）は、採用前に個別に判断する

## マイルストーン

| | 内容 | 状態 |
|---|---|---|
| M0 | リポジトリの雛形 | 完了 |
| M1 | 走査、URL・パスワード抽出、`--dry-run` | 未着手 |
| M2 | 公開ページの画像ダウンロードと状態管理 | 未着手 |
| M3 | cookies.txt 対応 | 未着手 |
| M4 | パスワード自動解除（`docs/privatter-notes.md` の調査後） | 未着手 |
| M5 | ブラウザ Cookie 直接読み込み、Linux 確認、自動実行 | 任意 |

## 動作確認の手順

### M0

```powershell
uv sync --locked
uv run auto-gleaner --version          # => auto-gleaner 0.0.1
uv run auto-gleaner run . --dry-run    # => 「まだ実装されていません」と表示され終了コード 2
uv run ruff check .
uv run pytest                 # => すべて passed
```

## ライセンス

MIT
