import pytest

from auto_gleaner import __version__
from auto_gleaner.cli import build_parser, main


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert __version__ in capsys.readouterr().out


def test_run_args_parse() -> None:
    args = build_parser().parse_args(["run", "some/root", "--dry-run", "-v"])
    assert args.command == "run"
    assert args.dry_run is True
    assert args.verbose is True
