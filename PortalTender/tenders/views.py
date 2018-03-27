from django.shortcuts import render, get_object_or_404, redirect
from .models import RzdTenders
from .forms import RzdTendersForm, RzdTendersAdditionForm

# Create your views here.

def rzd_tenders_query(request):
    rzd_query_all = RzdTenders.objects.all()
    return render(request, 'tenders/rzd_tenders.html', {'rzd_query_all': rzd_query_all})

def rzd_tenders_new(request):
    if request.method == "POST":
        form = RzdTendersForm(request.POST)
        if form.is_valid():
            rzd_query = form.save(commit=False)
            rzd_query.save()
            rzd_query.get_tenders()
            return redirect('rzd_tenders_found', pk=rzd_query.pk)
    else:
        form = RzdTendersForm()
    return render(request, 'tenders/rzd_tenders_new.html', {'form': form})

def rzd_tenders_found(request, pk):
    tender_query = get_object_or_404(RzdTenders, pk=pk)
    found_tender = tender_query.found_tenders.all()
    if request.method == "POST":
        form = RzdTendersAdditionForm(request.POST)
        if form.is_valid():
            found_tender = tender_query.found_tenders.filter(subject__contains=request.POST.get('addition_query'))
    else:
        form = RzdTendersAdditionForm()
    return render(request, 'tenders/rzd_tenders_found.html', {'tender_query': tender_query, 'found_tender': found_tender, 'form': form})