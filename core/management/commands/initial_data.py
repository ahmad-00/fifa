import logging

import pandas as pd
from django.core.management import BaseCommand
from django.db import connection

from core.models import Player
from core.utils import CurrencyToInt


class Command(BaseCommand):
    help = 'Inserts initial data'

    def handle(self, *args, **options):

        first_player = Player.objects.first()
        if first_player:
            logging.log(level=30, msg="Table 'player' is not empty. Initial data migration aborted")
            return

        cursor = connection.cursor()
        convertor = CurrencyToInt()
        breakpoint()
        prepared_list = ""
        sss = "("
        for i in range(1, 89):
            sss += "%s,"
        sss = sss[:-1]
        sss += ")"

        # Cleaning data
        fifa_data = pd.read_csv("data.csv", delimiter=',')
        fifa_data.fillna(0, inplace=True)
        fifa_data = fifa_data.drop('Index', 1)
        for i, line in fifa_data.iterrows():
            line[10] = convertor(value=line[10])
            line[11] = convertor(value=line[11])
            line[87] = convertor(value=line[87])
            prepared_list += cursor.mogrify(sss, tuple(line)).decode('utf-8') + ','

        cursor.execute(
            '''INSERT INTO player(public_id, name, age, photo, nationality, flag,overall, potential,club,club_logo,value,wage,special,preferred_foot,international_reputation,weak_foot,skill_moves,work_rate,body_type,real_face,position,jersey_number,joined,loaned_from,contract_valid_until,height,weight,ls,st,rs,lw,lf,cf,rf,rw,lam,cam,ram,lm,lcm,cm,rcm,rm,lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb,crossing,finishing,heading_accuracy,short_passing,volleys,dribbling,curve,fk_accuracy,long_passing,ball_control,acceleration,sprint_speed,agility,reactions,balance,shot_power,jumping,stamina,strength,long_shots,aggression,interceptions,positioning,vision,penalties,composure,marking,standing_tackle,sliding_tackle,gk_diving,gk_handling,gk_kicking,gk_positioning,gk_reflexes,release_clause) VALUES {}'''.format(
                prepared_list[:-1]))
        connection.commit()
