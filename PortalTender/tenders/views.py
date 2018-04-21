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
    found_tender_all = Tenders.objects.all()
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if 'reset' in request.POST:
            found_tender_all = Tenders.objects.all()
        elif 'search' in request.POST:
            if form.is_valid():
                found_tender_all = Tenders.objects.filter(subject__search=request.POST.get('addition_query'))
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

    return render(request, 'tenders/rzd_tenders_found.html', {'page': page, 'found_tender': found_tender, 'form': form})

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
        result = 'Удалено из избранного'
    except FavoriteTenders.DoesNotExist:
        fav_tend = FavoriteTenders.objects.create(user=user, fav_tender=tender)
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
    return render(request, 'tenders/favorites.html', {'tender_fav': tender_fav})