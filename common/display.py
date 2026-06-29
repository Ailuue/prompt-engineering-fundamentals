"""Tiny presentation helpers so the demos read nicely in a terminal."""


def rule(char: str = "-", width: int = 70) -> None:
    print(char * width)


def header(title: str) -> None:
    rule("=")
    print(title)
    rule("=")
