from fastapi import Header
from typing import Annotated


def get_foobar(foobar: Annotated[str, Header()]) -> str:
    return foobar


def get_header_foobar(header_name: str, default_value: str = "default"):
    def dependency(
        foobar: Annotated[str, Header(alias=header_name)] = default_value,
    ):
        return foobar

    return dependency
