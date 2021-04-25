# Generated by Django 3.1.7 on 2021-03-21 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0070_remove_router_last_deployment_id")]

    def create_ixp_connections(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        Connection = apps.get_model("net.Connection")
        InternetExchange = apps.get_model("peering.InternetExchange")
        InternetExchangePeeringSession = apps.get_model(
            "peering.InternetExchangePeeringSession"
        )

        for ixp in InternetExchange.objects.using(db_alias).all():
            connection = Connection.objects.using(db_alias).create(
                ipv4_address=ixp.ipv4_address,
                ipv6_address=ixp.ipv6_address,
                internet_exchange_point=ixp,
                router=ixp.router,
            )
            InternetExchangePeeringSession.objects.using(db_alias).filter(
                internet_exchange=ixp
            ).update(ixp_connection=connection)

    operations = [
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="ixp_connection",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="net.connection",
            ),
        ),
        migrations.RunPython(create_ixp_connections),
        migrations.RemoveField(model_name="internetexchange", name="ipv4_address"),
        migrations.RemoveField(model_name="internetexchange", name="ipv6_address"),
        migrations.RemoveField(
            model_name="internetexchange", name="peeringdb_netixlan"
        ),
        migrations.RemoveField(model_name="internetexchange", name="peeringdb_ix"),
        migrations.RemoveField(model_name="internetexchange", name="router"),
        migrations.AddField(
            model_name="internetexchange",
            name="peeringdb_ixlan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="peeringdb.ixlan",
            ),
        ),
        migrations.AlterModelOptions(
            name="internetexchangepeeringsession",
            options={"ordering": ["autonomous_system", "ixp_connection", "ip_address"]},
        ),
        migrations.RemoveField(
            model_name="internetexchangepeeringsession",
            name="internet_exchange",
        ),
    ]