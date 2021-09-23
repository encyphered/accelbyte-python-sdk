import json

import click

from accelbyte_py_sdk.api.iam import admin_delete_user_permission_bulk_v3
from accelbyte_py_sdk.api.iam.models import ModelPermissionDeleteRequest

from ._utils import login_client


@click.command()
@click.argument("user_id")
@click.argument("body")
@click.option("--namespace")
@click.option("--doc", type=bool)
def delete_user_permissions(
        user_id,
        body,
        namespace,
        doc,
):
    login_client()
    if doc:
        click.echo(admin_delete_user_permission_bulk_v3.__doc__)
    body = json.loads(body)
    body = [ModelPermissionDeleteRequest.create_from_dict(b) for b in body]
    result, error = admin_delete_user_permission_bulk_v3(
        body=body,
        user_id=user_id,
        namespace=namespace,
    )
    if error:
        raise Exception(str(error))
    click.echo("Delete user permissions success.")
