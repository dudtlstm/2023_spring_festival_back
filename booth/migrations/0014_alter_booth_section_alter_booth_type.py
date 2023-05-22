# Generated by Django 4.2.1 on 2023-05-22 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booth", "0013_alter_booth_section"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booth",
            name="section",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="booth",
            name="type",
            field=models.CharField(
                choices=[
                    ("주간부스", "주간부스"),
                    ("야간부스", "야간부스"),
                    ("플리마켓", "플리마켓"),
                    ("푸드트럭", "푸드트럭"),
                    ("학교부스", "학교부스"),
                    ("외부부스", "외부부스"),
                ],
                max_length=10,
            ),
        ),
    ]
