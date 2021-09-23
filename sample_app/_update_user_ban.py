import click

from accelbyte_py_sdk.api.iam import admin_update_user_ban_v3
from accelbyte_py_sdk.api.iam.models import ModelBanUpdateRequest

from ._utils import login_client


@click.command()
@click.argument("user_id")
@click.argument("ban_id")
@click.argument("enabled")
@click.option("--namespace")
@click.option("--skip_notif", type=bool, default=True)
@click.option("--doc", type=bool)
def update_user_ban(
        user_id,
        ban_id,
        enabled,
        namespace,
        skip_notif,
        doc,
):
    login_client()
    if doc:
        click.echo(admin_update_user_ban_v3.__doc__)
    result, error = admin_update_user_ban_v3(
        body=ModelBanUpdateRequest.create(
            enabled=enabled,
            skip_notif=skip_notif,
        ),
        user_id=user_id,
        ban_id=ban_id,
        namespace=namespace,
    )
    if error:
        raise Exception(str(error))
    click.echo("Update user ban success.")
