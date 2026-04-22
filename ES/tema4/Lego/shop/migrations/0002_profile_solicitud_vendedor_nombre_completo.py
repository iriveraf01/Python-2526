from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="solicitud_vendedor",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="nombre_completo",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

