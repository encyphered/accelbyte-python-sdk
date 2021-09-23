import yaml

import click

from accelbyte_py_sdk.api.iam import admin_update_role_v3
from accelbyte_py_sdk.api.iam.models import ModelRoleUpdateRequestV3

from ._utils import login_user


@click.command()
@click.argument("role_id")
@click.argument("role_name")
@click.argument("is_wildcard", type=bool, default=True)
@click.option("--doc", type=bool)
def update_role(
        role_id,
        role_name,
        is_wildcard,
        doc,
):
    login_user(None, None)
    if doc:
        click.echo(admin_update_role_v3.__doc__)
    result, error = admin_update_role_v3(
        body=ModelRoleUpdateRequestV3.create(
            is_wildcard=is_wildcard,
            role_name=role_name,
        ),
        role_id=role_id,
    )
    if error:
        raise Exception(str(error))
    click.echo("Update role success.")
    click.echo(yaml.safe_dump(result.to_dict()))