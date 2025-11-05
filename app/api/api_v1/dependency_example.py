from typing import Annotated
from fastapi import APIRouter, Depends, Header
from api.api_v1.dependencies.func_dep import get_foobar, get_header_foobar
from utils.helper import GreatHelper

router = APIRouter(prefix="/dependency-example")


@router.get("/single-direct-dependency")
def single_direct_dependency(foobar: str = Depends(get_foobar)):
    return {"foobar": foobar}


@router.get("/master-hoe-fucking-dependency")
def master_hoe_fucking_dependency(
    foobar: Annotated[str, Depends(get_header_foobar("foobar"))],
    hui: Annotated[str, Depends(get_header_foobar("hui"))],
):
    return {"foobar": foobar, "hui": hui}


@router.get("/seemless-dependency")
def seemless_dependency(
    helper_name: Annotated[str, Depends(get_header_foobar("helper_name"))],
):
    helper = GreatHelper(name=helper_name, default="default")
    return helper.as_dict()
