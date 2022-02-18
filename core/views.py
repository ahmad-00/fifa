import psycopg2.extras
from django.db import connections
from django.http import HttpResponse
from django.template import loader

from core.helper.find_player import find_player
from core.models import Player


def search(request):
    name = request.GET.get('name', None)
    nationality = request.GET.get('nationality', None)
    club = request.GET.get('club', None)
    limit = request.GET.get('limit', 20)
    offset = request.GET.get('offset', 0)
    context = {}
    template = loader.get_template('search.html')

    limit = int(limit)
    offset = int(offset)
    if name or club or name:
        query = Player.objects.values('name', 'nationality', 'club', 'age', 'photo', 'overall', 'value')
        if name and len(name) > 3:
            query = query.filter(name__search=name)
        if nationality and len(nationality) > 3:
            query = query.filter(nationality__search=nationality)
        if club and len(club) > 3:
            query = query.filter(club__search=club)

        query = query.all()[offset:limit + offset]
        context['result'] = list(query)

    return HttpResponse(template.render(context, request))


def team_builder(request):
    generic_error_message = "Building team failed"
    budget = request.GET.get('budget', None)
    context = {'request_url': 'team_builder'}
    template = loader.get_template('teamBuilder.html')

    if not budget:
        return HttpResponse(template.render(context, request))
    budget = int(budget)

    # Because there were no reference of how to distribute the budget.
    # I decided to distribute it equally for each player

    goal_keeper_budget = budget / 11
    goal_keeper = find_player(
        position_category='GK',
        budget=goal_keeper_budget,
        quantity=1
    )
    if len(goal_keeper) != 1:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - goal_keeper[0]['player_fee']

    fullback_budget = budget / 10
    fullbacks = find_player(
        position_category='FB',
        budget=fullback_budget,
        quantity=2
    )
    if len(fullbacks) != 2:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - (fullbacks[0]['player_fee'] + fullbacks[1]['player_fee'])

    halfback_budget = budget / 8
    halfbacks = find_player(
        position_category='HB',
        budget=halfback_budget,
        quantity=3
    )
    if len(halfbacks) != 3:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - (halfbacks[0]['player_fee'] + halfbacks[1]['player_fee'] + halfbacks[2]['player_fee'])

    forward_budget = budget / 5
    forwards = find_player(
        position_category='FW',
        budget=forward_budget,
        quantity=5
    )
    if len(forwards) != 5:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))

    context['selected_players'] = {
        'goal_keeper': goal_keeper,
        'fullbacks': fullbacks,
        'halfbacks': halfbacks,
        'forwards': forwards
    }

    return HttpResponse(template.render(context, request))


def team_builder2(request):
    generic_error_message = "Building team failed"
    budget = request.GET.get('budget', None)
    context = {'request_url': 'team_builder2'}
    template = loader.get_template('teamBuilder.html')

    if not budget:
        return HttpResponse(template.render(context, request))
    budget = int(budget)

    conn = connections['default']  # cursor_factory does not work using default provided connection
    conn.ensure_connection()
    with conn.connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor
    ) as cursor:  # This cursor_factory changes tuple result to dict
        cursor.execute(
            '''SELECT * FROM (SELECT ROW_NUMBER() OVER (PARTITION BY position_category ORDER BY overall desc) AS r, name, nationality, club, age, photo, overall, value, release_clause, position_category FROM player where position_category != '' and (value + release_clause) <= %s) x WHERE x.r <= 5;''',
            (budget,))
        players = cursor.fetchall()

    if len(players) < 11:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))

    quantity_map = {
        "GK": 1,
        "FB": 2,
        "HB": 3,
        "FW": 5
    }
    players_map = {
        "GK": [],
        "FB": [],
        "HB": [],
        "FW": []
    }

    for player in players:
        position_category = player['position_category']
        if len(players_map[position_category]) < quantity_map[position_category]:
            players_map[position_category].append(player)

    for key, value in players_map.items():
        if len(value) < quantity_map[key]:
            print(key)
            context['error'] = generic_error_message
            return HttpResponse(template.render(context, request))

    context['selected_players'] = {
        'goal_keeper': players_map['GK'],
        'fullbacks': players_map['FB'],
        'halfbacks': players_map['HB'],
        'forwards': players_map['FW']
    }
    return HttpResponse(template.render(context, request))


'''
There are other implementation with more optimal overall calculation. There are multiple issues when using those methods:
    # All data be retrieved from db.Specially for huge number of rows that has ready bad performance and uses a lot of memory, which is not practical.
    # These method are have bad performance(O notation) because of many for loops.
'''
