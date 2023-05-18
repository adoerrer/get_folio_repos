from typing import Literal, List, Dict, Union

from pydantic import BaseModel, validator
import requests

OVERRIDES: Dict[str, str] = {
    "mod-z3950": "Net-Z3950-FOLIO"
}


class ModulAction(BaseModel):
    id: str
    action: str


class ModulInstallAction(ModulAction):
    action: Literal["enable"]


class RepositoryAtTag(BaseModel):
    repo_scheme: str = "https"
    repo_url: str = "github.com"
    repo_user: str = "folio-org"
    repo_name: str
    repo_tag: str

    @validator("repo_tag")
    def check_tag_exists(cls, v: str, values) -> str:  # noqa
        r = requests.head(
            f"{values['repo_scheme']}://{values['repo_url']}/{values['repo_user']}/{values['repo_name']}/tree/{v}")
        if r.status_code == 200:
            return v
        raise ValueError(f"Unknown Tag {v} for {values['repo_name']}")


def modul_install_action_list_to_repository_at_tag_list(
        data: Union[List[ModulInstallAction], List[Dict[str, str]]],
) -> List[RepositoryAtTag]:
    if not all(isinstance(o, ModulInstallAction) for o in data):
        data = [ModulInstallAction.parse_obj(conv) for conv in data]
    id_list = [action.id.rpartition("-") for action in
               data]
    return [
        RepositoryAtTag(repo_name=OVERRIDES[entry[0]] if entry[0] in OVERRIDES else entry[0], repo_tag=f"v{entry[2]}")
        for entry in id_list
    ]
