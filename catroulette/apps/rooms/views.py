"""
.. module:: catroulette.apps.rooms.views
   :synopsis: CatRoulette Room Views.

.. moduleauthor:: Alex Kavanaugh <kavanaugh.development@outlook.com>

"""

from django.contrib.auth import get_user_model as get_cat_model
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from django_ajax.decorators import ajax

from .utils import match_cat


@ajax
@csrf_exempt
@require_POST
def get_room(request):
    """
    Cat posted personality details. Create a cat object in the
    database with those details and attempt to find a match
    """

    vocalness = request.POST["vocalness"]
    intelligence = request.POST["intelligence"]
    energy = request.POST["energy"]

    new_cat = get_cat_model()(vocalness=vocalness, intelligence=intelligence, energy=energy)
    new_cat.save()

    return {"room_name": match_cat(new_cat)}
