import argparse

from mock import Mock, patch
from pytest import raises

from repo_management import argparse as repo_argparse


def test_argparsefactory__init__() -> None:
    assert isinstance(repo_argparse.ArgParseFactory().parser, argparse.ArgumentParser)


def test_argparsefactory__db2json() -> None:
    assert isinstance(repo_argparse.ArgParseFactory.db2json(), argparse.ArgumentParser)


def test_argparsefactory__json2db() -> None:
    assert isinstance(repo_argparse.ArgParseFactory.json2db(), argparse.ArgumentParser)


@patch(
    "repo_management.argparse.Path",
    Mock(return_value=Mock(exists=Mock(side_effect=[False, True, True]), is_file=Mock(side_effect=[False, True]))),
)
def test_argparsefactory_string_to_file_path() -> None:
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_file_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_file_path("foo")
    assert repo_argparse.ArgParseFactory.string_to_file_path("foo")


@patch(
    "os.access",
    Mock(side_effect=[False, False, True, True]),
)
@patch("repo_management.argparse.Path.exists", Mock(side_effect=[True, True, False, False, False, True, False]))
@patch("repo_management.argparse.Path.is_file", Mock(side_effect=[False, True, True]))
@patch("repo_management.argparse.Path.parent", return_value=Mock())
def test_argparsefactory_string_to_writable_file_path(parent_mock: Mock) -> None:
    parent_mock.exists.side_effect = [False, True, True, True]
    parent_mock.is_dir.side_effect = [False, True, True]
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    assert repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")
    assert repo_argparse.ArgParseFactory.string_to_writable_file_path("foo")


@patch(
    "repo_management.argparse.Path",
    Mock(return_value=Mock(exists=Mock(side_effect=[False, True, True]), is_dir=Mock(side_effect=[False, True]))),
)
def test_argparsefactory_string_to_dir_path() -> None:
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_dir_path("foo")
    with raises(argparse.ArgumentTypeError):
        repo_argparse.ArgParseFactory.string_to_dir_path("foo")
    assert repo_argparse.ArgParseFactory.string_to_dir_path("foo")
