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
    context = {}
    template = loader.get_template('teamBuilder.html')

    if not budget:
        return HttpResponse(template.render(context, request))
    budget = int(budget)

    # Because there were no reference of how to distribute the budget. I decided to distribute it equally for each player
    goal_keeper_budget = budget / 11
    goal_keeper = find_player(
        positions=['GK'],
        budget=goal_keeper_budget,
        quantity=1
    )
    if len(goal_keeper) != 1:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - goal_keeper[0]['player_fee']

    fullback_budget = budget / 10
    fullbacks = find_player(
        positions=['LB', 'RB', 'LWB', 'RWB'],
        budget=fullback_budget,
        quantity=2
    )
    if len(fullbacks) != 2:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - (fullbacks[0]['player_fee'] + fullbacks[1]['player_fee'])

    halfback_budget = budget / 8
    halfbacks = find_player(
        positions=['CB', 'LCB', 'RCB', 'CDM', 'LDM', 'RDM', 'CM', 'LCM', 'RCM', 'LM', 'RM'],
        budget=halfback_budget,
        quantity=3
    )
    if len(halfbacks) != 3:
        context['error'] = generic_error_message
        return HttpResponse(template.render(context, request))
    budget = budget - (halfbacks[0]['player_fee'] + halfbacks[1]['player_fee'] + halfbacks[2]['player_fee'])

    forward_budget = budget / 5
    forwards = find_player(
        positions=['CAM', 'LAM', 'RAM', 'LWF', 'RWF', 'CF', 'LCF', 'RCF'],
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


'''
There are other implementation with more optimal overall calculation. There are multiple issues when using those methods:
    # All data be retrieved from db.Specially for huge number of rows that has ready bad performance and uses a lot of memory, which is not practical.
    # These method are have bad performance(O notation) because of many for loops.
'''
