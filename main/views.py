from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request):
    return render(request, 'main/index.html')


def other_page(request, page: str):
    parts_url = ['main/', '.html']
    try:
        template = get_template(page.join(parts_url))
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


"""
typing hunting - go!!!
"""