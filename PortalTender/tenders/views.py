from django.shortcuts import render, get_object_or_404, redirect
from .models import Tenders, FavoriteTenders
from .forms import RzdTendersAdditionForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse
import json

@login_required
def dashboard(request):
    return render(request, 'tenders/dashboard.html')

@login_required
def rzd_tenders_found(request):
    addition_query = request.GET.get('addition_query')
    if addition_query:
        found_tender_all = Tenders.objects.filter(etp='РЖД').filter(subject__search=addition_query)
    else:
        found_tender_all = Tenders.objects.filter(etp='РЖД')
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.filter(etp='РЖД')
        elif 'search' in request.POST:
            if form.is_valid():
                addition_query = request.POST.get('addition_query')
                found_tender_all = Tenders.objects.filter(etp='РЖД').filter(subject__search=addition_query)
    else:
        form = RzdTendersAdditionForm()

    paginator = Paginator(found_tender_all, 25)
    page = request.GET.get('page')
    try:
        found_tender = paginator.page(page)
    except PageNotAnInteger:
        found_tender = paginator.page(1)
    except EmptyPage:
        found_tender = paginator.page(paginator.num_pages)

    return render(request, 'tenders/rzd_tenders_found.html', {'page': page, 'found_tender': found_tender, 'form': form, 'addition_query': addition_query})

@login_required
def rosseti_tenders_found(request):
    addition_query = request.GET.get('addition_query')
    if addition_query:
        found_tender_all = Tenders.objects.filter(etp='Россети').filter(subject__search=addition_query)
    else:
        found_tender_all = Tenders.objects.filter(etp='Россети')
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.filter(etp='Россети')
        elif 'search' in request.POST:
            if form.is_valid():
                addition_query = request.POST.get('addition_query')
                found_tender_all = Tenders.objects.filter(etp='Россети').filter(subject__search=addition_query)
    else:
        form = RzdTendersAdditionForm()

    paginator = Paginator(found_tender_all, 25)
    page = request.GET.get('page')
    try:
        found_tender = paginator.page(page)
    except PageNotAnInteger:
        found_tender = paginator.page(1)
    except EmptyPage:
        found_tender = paginator.page(paginator.num_pages)

    return render(request, 'tenders/rosseti_tenders_found.html', {'page': page, 'found_tender': found_tender, 'form': form, 'addition_query': addition_query})

@login_required
def rosatom_tenders_found(request):
    addition_query = request.GET.get('addition_query')
    if addition_query:
        found_tender_all = Tenders.objects.filter(etp='Росатом').filter(subject__search=addition_query)
    else:
        found_tender_all = Tenders.objects.filter(etp='Росатом')
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.filter(etp='Росатом')
        elif 'search' in request.POST:
            if form.is_valid():
                addition_query = request.POST.get('addition_query')
                found_tender_all = Tenders.objects.filter(etp='Росатом').filter(subject__search=addition_query)
    else:
        form = RzdTendersAdditionForm()

    paginator = Paginator(found_tender_all, 25)
    page = request.GET.get('page')
    try:
        found_tender = paginator.page(page)
    except PageNotAnInteger:
        found_tender = paginator.page(1)
    except EmptyPage:
        found_tender = paginator.page(paginator.num_pages)

    return render(request, 'tenders/rosatom_tenders_found.html', {'page': page, 'found_tender': found_tender, 'form': form, 'addition_query': addition_query})



@login_required
def gazprom_tenders_found(request):
    addition_query = request.GET.get('addition_query')
    if addition_query:
        found_tender_all = Tenders.objects.filter(etp='Газпром').filter(subject__search=addition_query)
    else:
        found_tender_all = Tenders.objects.filter(etp='Газпром')
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.filter(etp='Газпром')
        elif 'search' in request.POST:
            if form.is_valid():
                addition_query = request.POST.get('addition_query')
                found_tender_all = Tenders.objects.filter(etp='Газпром').filter(subject__search=addition_query)
    else:
        form = RzdTendersAdditionForm()

    paginator = Paginator(found_tender_all, 25)
    page = request.GET.get('page')
    try:
        found_tender = paginator.page(page)
    except PageNotAnInteger:
        found_tender = paginator.page(1)
    except EmptyPage:
        found_tender = paginator.page(paginator.num_pages)

    return render(request, 'tenders/gazprom_tenders_found.html', {'page': page, 'found_tender': found_tender, 'form': form, 'addition_query': addition_query})

@login_required
def all_tenders(request):
    addition_query = request.GET.get('addition_query')
    if addition_query:
        found_tender_all = Tenders.objects.all().filter(subject__search=addition_query)
    else:
        found_tender_all = Tenders.objects.all()
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.all()
        elif 'search' in request.POST:
            if form.is_valid():
                addition_query = request.POST.get('addition_query')
                found_tender_all = Tenders.objects.all().filter(subject__search=addition_query)
    else:
        form = RzdTendersAdditionForm()

    paginator = Paginator(found_tender_all, 25)
    page = request.GET.get('page')
    try:
        found_tender = paginator.page(page)
    except PageNotAnInteger:
        found_tender = paginator.page(1)
    except EmptyPage:
        found_tender = paginator.page(paginator.num_pages)

    return render(request, 'tenders/all_tenders.html', {'page': page, 'found_tender': found_tender, 'form': form, 'addition_query': addition_query})


@login_required
def tender_detail(request, pk):
    tender = get_object_or_404(Tenders, pk=pk)
    return render(request, 'tenders/tender_detail.html', {'tender': tender})

# @login_required
# def add_remove_favorite(request, pk):
#     user = request.user
#     tender = Tenders.objects.get(pk=pk)
#     try:
#         fav_tend = FavoriteTenders.objects.get(user=user, fav_tender=tender)
#         fav_tend.delete()
#     except FavoriteTenders.DoesNotExist:
#         fav_tend = FavoriteTenders.objects.create(user=user, fav_tender=tender)
#         fav_tend.save()
#     # return redirect('tenders/tender_detail.html', pk=pk)
#     return render(request, 'tenders/tender_detail.html', {'tender': get_object_or_404(Tenders, pk=pk)})

#Добавление в избранное с помощью AJAX
@login_required
def add_remove_favorite(request, pk):
    user = request.user
    tender = Tenders.objects.get(pk=pk)
    try:
        fav_tend = FavoriteTenders.objects.get(user=user, fav_tender=tender)
        fav_tend.delete()
        tender.in_favorite = False
        tender.save()
        result = 'Удалено из избранного'
    except FavoriteTenders.DoesNotExist:
        fav_tend = FavoriteTenders.objects.create(user=user, fav_tender=tender)
        tender.in_favorite = True
        tender.save()
        fav_tend.save()
        result = 'Добавленов в избранное'

    return HttpResponse(
        json.dumps({
            'result': result,
        }),
        content_type='application/json'
    )

@login_required
def in_favorite(request, pk):
    user = request.user
    tender = Tenders.objects.get(pk=pk)
    button_name = 'В избранное'
    if FavoriteTenders.objects.filter(user=user, fav_tender=tender).exists():
        button_name = 'Удалить из Избранного'

    return HttpResponse(
        json.dumps({
            'button_name': button_name,
        }),
        content_type='application/json'
    )

@login_required
def favorites(request):
    user = request.user
    user_favorite = FavoriteTenders.objects.filter(user=user)
    tender_fav = []
    for uf in user_favorite:
        tender_fav.append(uf.fav_tender)
    paginator = Paginator(tender_fav, 25)
    page = request.GET.get('page')
    try:
        tender_fav = paginator.page(page)
    except PageNotAnInteger:
        tender_fav = paginator.page(1)
    except EmptyPage:
        tender_fav = paginator.page(paginator.num_pages)

    return render(request, 'tenders/favorites.html', {'page': page, 'tender_fav': tender_fav})

