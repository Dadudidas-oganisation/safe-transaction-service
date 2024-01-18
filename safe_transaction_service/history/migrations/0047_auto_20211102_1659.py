# Generated by Django 3.2.7 on 2021-11-02 16:59

from django.db import migrations
from django.db.models import Count


def _remove_duplicated(TokenTransferModel):
    for transfer in (
        TokenTransferModel.objects.values_list("ethereum_tx", "log_index")
        .annotate(c=Count("*"))
        .filter(c__gt=1)
    ):
        for transfer_to_delete in list(
            TokenTransferModel.objects.filter(
                ethereum_tx_id=transfer[0], log_index=transfer[1]
            )[1:]
        ):
            transfer_to_delete.delete()


def remove_duplicated(apps, schema_editor):
    ERC20Transfer = apps.get_model("history", "ERC20Transfer")
    ERC721Transfer = apps.get_model("history", "ERC721Transfer")

    _remove_duplicated(ERC20Transfer)
    _remove_duplicated(ERC721Transfer)


class Migration(migrations.Migration):
    dependencies = [
        ("history", "0046_delete_ethereumevent"),
    ]

    operations = [
        migrations.RunPython(remove_duplicated, reverse_code=migrations.RunPython.noop),
        migrations.AlterUniqueTogether(
            name="erc20transfer",
            unique_together={("ethereum_tx", "log_index")},
        ),
        migrations.AlterUniqueTogether(
            name="erc721transfer",
            unique_together={("ethereum_tx", "log_index")},
        ),
    ]
