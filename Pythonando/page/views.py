from django.shortcuts import render
from .models import Usuario
from django.core.paginator import Paginator

def pagination(request):
    usuarios = Usuario.objects.all()

    usuario_paginator = Paginator(usuarios, 2)
    page_num = request.GET.get('page')
    page = usuario_paginator.get_page(page_num)

    return render(request, 'pagination.html', {'page': page})
