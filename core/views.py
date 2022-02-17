from django.http import HttpResponse

from django.template import loader

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
    if club or name or name:
        query = Player.objects
        if name and len(name) > 3:
            query = query.filter(name__search=name)
        if nationality and len(nationality) > 3:
            query = query.filter(nationality__search=nationality)
        if club and len(club) > 3:
            query = query.filter(club__search=club)

        query = query.all()[offset:limit + offset]
        context['result'] = list(query)

    return HttpResponse(template.render(context, request))
