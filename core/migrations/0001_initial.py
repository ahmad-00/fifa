# Generated by Django 4.0.2 on 2022-02-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField()),
                ('photo', models.CharField(blank=True, max_length=200, null=True)),
                ('nationality', models.CharField(max_length=50)),
                ('flag', models.CharField(max_length=200, null=True)),
                ('overall', models.SmallIntegerField()),
                ('potential', models.SmallIntegerField()),
                ('club', models.CharField(max_length=50)),
                ('club_logo', models.CharField(max_length=200)),
                ('value', models.IntegerField()),
                ('wage', models.IntegerField()),
                ('special', models.IntegerField()),
                ('preferred_foot', models.CharField(max_length=5)),
                ('international_reputation', models.SmallIntegerField()),
                ('weak_foot', models.SmallIntegerField()),
                ('skill_moves', models.SmallIntegerField()),
                ('work_rate', models.CharField(max_length=30)),
                ('body_type', models.CharField(max_length=30)),
                ('real_face', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=3)),
                ('jersey_number', models.SmallIntegerField()),
                ('joined', models.CharField(max_length=20, null=True)),
                ('loaned_from', models.CharField(max_length=50)),
                ('contract_valid_until', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=6)),
                ('weight', models.CharField(max_length=6)),
                ('ls', models.CharField(max_length=4)),
                ('st', models.CharField(max_length=4)),
                ('rs', models.CharField(max_length=4)),
                ('lw', models.CharField(max_length=4)),
                ('lf', models.CharField(max_length=4)),
                ('cf', models.CharField(max_length=4)),
                ('rf', models.CharField(max_length=4)),
                ('rw', models.CharField(max_length=4)),
                ('lam', models.CharField(max_length=4)),
                ('cam', models.CharField(max_length=4)),
                ('ram', models.CharField(max_length=4)),
                ('lm', models.CharField(max_length=4)),
                ('lcm', models.CharField(max_length=4)),
                ('cm', models.CharField(max_length=4)),
                ('rcm', models.CharField(max_length=4)),
                ('rm', models.CharField(max_length=4)),
                ('lwb', models.CharField(max_length=4)),
                ('ldm', models.CharField(max_length=4)),
                ('cdm', models.CharField(max_length=4)),
                ('rdm', models.CharField(max_length=4)),
                ('rwb', models.CharField(max_length=4)),
                ('lb', models.CharField(max_length=4)),
                ('lcb', models.CharField(max_length=4)),
                ('cb', models.CharField(max_length=4)),
                ('rcb', models.CharField(max_length=4)),
                ('rb', models.CharField(max_length=4)),
                ('crossing', models.SmallIntegerField()),
                ('finishing', models.SmallIntegerField()),
                ('heading_accuracy', models.SmallIntegerField()),
                ('short_passing', models.SmallIntegerField()),
                ('volleys', models.SmallIntegerField()),
                ('dribbling', models.SmallIntegerField()),
                ('curve', models.SmallIntegerField()),
                ('fk_accuracy', models.SmallIntegerField()),
                ('long_passing', models.SmallIntegerField()),
                ('ball_control', models.SmallIntegerField()),
                ('acceleration', models.SmallIntegerField()),
                ('sprint_speed', models.SmallIntegerField()),
                ('agility', models.SmallIntegerField()),
                ('reactions', models.SmallIntegerField()),
                ('balance', models.SmallIntegerField()),
                ('shot_power', models.SmallIntegerField()),
                ('jumping', models.SmallIntegerField()),
                ('stamina', models.SmallIntegerField()),
                ('strength', models.SmallIntegerField()),
                ('long_shots', models.SmallIntegerField()),
                ('aggression', models.SmallIntegerField()),
                ('interceptions', models.SmallIntegerField()),
                ('positioning', models.SmallIntegerField()),
                ('vision', models.SmallIntegerField()),
                ('penalties', models.SmallIntegerField()),
                ('composure', models.SmallIntegerField()),
                ('marking', models.SmallIntegerField()),
                ('standing_tackle', models.SmallIntegerField()),
                ('sliding_tackle', models.SmallIntegerField()),
                ('gk_diving', models.SmallIntegerField()),
                ('gk_handling', models.SmallIntegerField()),
                ('gk_kicking', models.SmallIntegerField()),
                ('gk_positioning', models.SmallIntegerField()),
                ('gk_reflexes', models.SmallIntegerField()),
                ('release_clause', models.IntegerField()),
            ],
            options={
                'db_table': 'player',
            },
        ),
    ]