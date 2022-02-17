from typing import List, Union

from django.db.models import F

from core.models import Player


def find_player(positions: List[str], budget: Union[float, int], quantity: int) -> List[dict]:
    players = Player.objects.values(
        'name', 'nationality', 'club', 'age', 'photo', 'overall', 'value', 'release_clause', 'position'
    )
    if len(positions) == 1:
        players = players.filter(
            position=positions[0]
        )
    else:
        players = players.filter(
            position__in=positions
        )

    players = players.annotate(
        player_fee=F('value') + F('release_clause')
    ).filter(
        player_fee__lte=budget
    ).order_by(
        '-overall'
    )
    if quantity == 1:
        players = players.first()
        return [players]
    else:
        players = players.all()[0:quantity]
        return list(players)
