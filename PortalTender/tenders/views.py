from django.shortcuts import render, get_object_or_404, redirect
from .models import Tenders
from .forms import RzdTendersAdditionForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

# Create your views here.

# @login_required
# def rzd_tenders_query(request):
#     rzd_query_all = RzdTenders.objects.all()
#     return render(request, 'tenders/rzd_tenders.html', {'rzd_query_all': rzd_query_all})

# @login_required
# def rzd_tenders_new(request):
#     if request.method == "POST":
#         form = RzdTendersForm(request.POST)
#         if form.is_valid():
#             rzd_query = form.save(commit=False)
#             rzd_query.save()
#             try:
#                 rzd_query.get_tenders()
#             except:
#                 return render(request, 'tenders/tanders_not_found.html')
#             return redirect('rzd_tenders_found', pk=rzd_query.pk)
#     else:
#         form = RzdTendersForm()
#     return render(request, 'tenders/rzd_tenders_new.html', {'form': form})

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