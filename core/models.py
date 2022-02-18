from django.contrib.postgres.indexes import GinIndex, HashIndex
from django.db import models

'''
I had too choose between one table with all rows and multiple tables with fewer rows.
Considering high rate of writes on db and having almost all columns available for every player,
I decided it's better to use single table.
It would improve performance specially for write operation since there won't be multiple request for db for creating
related fields.
'''


class Player(models.Model):
    public_id = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField(null=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=50)
    flag = models.CharField(max_length=200, null=True)
    overall = models.SmallIntegerField(null=True)
    potential = models.SmallIntegerField(null=True)
    club = models.CharField(max_length=50, null=True)
    club_logo = models.CharField(max_length=200, null=True)
    value = models.IntegerField(null=True)
    wage = models.IntegerField(null=True)
    special = models.IntegerField(null=True)
    preferred_foot = models.CharField(max_length=5, null=True)
    international_reputation = models.SmallIntegerField(null=True)
    weak_foot = models.SmallIntegerField(null=True)
    skill_moves = models.SmallIntegerField(null=True)
    work_rate = models.CharField(max_length=30, null=True)
    body_type = models.CharField(max_length=30, null=True)
    real_face = models.CharField(max_length=3, null=True)
    position = models.CharField(max_length=3, null=True)
    position_category = models.CharField(max_length=2, null=True)
    jersey_number = models.SmallIntegerField(null=True)
    joined = models.CharField(max_length=20, null=True)
    loaned_from = models.CharField(max_length=50, null=True)
    contract_valid_until = models.CharField(max_length=20, null=True)
    height = models.CharField(max_length=8, null=True)
    weight = models.CharField(max_length=6, null=True)
    ls = models.CharField(max_length=4, null=True)
    st = models.CharField(max_length=4, null=True)
    rs = models.CharField(max_length=4, null=True)
    lw = models.CharField(max_length=4, null=True)
    lf = models.CharField(max_length=4, null=True)
    cf = models.CharField(max_length=4, null=True)
    rf = models.CharField(max_length=4, null=True)
    rw = models.CharField(max_length=4, null=True)
    lam = models.CharField(max_length=4, null=True)
    cam = models.CharField(max_length=4, null=True)
    ram = models.CharField(max_length=4, null=True)
    lm = models.CharField(max_length=4, null=True)
    lcm = models.CharField(max_length=4, null=True)
    cm = models.CharField(max_length=4, null=True)
    rcm = models.CharField(max_length=4, null=True)
    rm = models.CharField(max_length=4, null=True)
    lwb = models.CharField(max_length=4, null=True)
    ldm = models.CharField(max_length=4, null=True)
    cdm = models.CharField(max_length=4, null=True)
    rdm = models.CharField(max_length=4, null=True)
    rwb = models.CharField(max_length=4, null=True)
    lb = models.CharField(max_length=4, null=True)
    lcb = models.CharField(max_length=4, null=True)
    cb = models.CharField(max_length=4, null=True)
    rcb = models.CharField(max_length=4, null=True)
    rb = models.CharField(max_length=4, null=True)
    crossing = models.SmallIntegerField(null=True)
    finishing = models.SmallIntegerField(null=True)
    heading_accuracy = models.SmallIntegerField(null=True)
    short_passing = models.SmallIntegerField(null=True)
    volleys = models.SmallIntegerField(null=True)
    dribbling = models.SmallIntegerField(null=True)
    curve = models.SmallIntegerField(null=True)
    fk_accuracy = models.SmallIntegerField(null=True)
    long_passing = models.SmallIntegerField(null=True)
    ball_control = models.SmallIntegerField(null=True)
    acceleration = models.SmallIntegerField(null=True)
    sprint_speed = models.SmallIntegerField(null=True)
    agility = models.SmallIntegerField(null=True)
    reactions = models.SmallIntegerField(null=True)
    balance = models.SmallIntegerField(null=True)
    shot_power = models.SmallIntegerField(null=True)
    jumping = models.SmallIntegerField(null=True)
    stamina = models.SmallIntegerField(null=True)
    strength = models.SmallIntegerField(null=True)
    long_shots = models.SmallIntegerField(null=True)
    aggression = models.SmallIntegerField(null=True)
    interceptions = models.SmallIntegerField(null=True)
    positioning = models.SmallIntegerField(null=True)
    vision = models.SmallIntegerField(null=True)
    penalties = models.SmallIntegerField(null=True)
    composure = models.SmallIntegerField(null=True)
    marking = models.SmallIntegerField(null=True)
    standing_tackle = models.SmallIntegerField(null=True)
    sliding_tackle = models.SmallIntegerField(null=True)
    gk_diving = models.SmallIntegerField(null=True)
    gk_handling = models.SmallIntegerField(null=True)
    gk_kicking = models.SmallIntegerField(null=True)
    gk_positioning = models.SmallIntegerField(null=True)
    gk_reflexes = models.SmallIntegerField(null=True)
    release_clause = models.IntegerField(null=True)

    class Meta:
        # GinIndex is used because tsvector is used for search.
        db_table = "player"
        indexes = [
            GinIndex(fields=('name',)),
            GinIndex(fields=('club',)),
            GinIndex(fields=('nationality',)),
            HashIndex(fields=('position_category',))
        ]
