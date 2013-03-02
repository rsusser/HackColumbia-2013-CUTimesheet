from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import Sheet, Week, Day
from forms import SheetForm


@login_required
def index(request):
    return HttpResponse("Columbia wind login request page goes here.")

@login_required
def list(request, user_id):
    return HttpResponse("This is a record of current/recent timesheets for %s." %user_id)

def create(request, sheet_id):
#    return HttpResponse("You have started a new timesheet, %s." %sheet_id)
    if request.method == 'POST':
        form = SheetForm(request.POST)
#        if form.is_valid():
        form.save()

            #validation rules
#        st1=form.cleaned_data['st1']
#        et1=form.cleaned_data['end_time']
#        st2=form.cleaned_data['start_time2']
#        et2=form.cleaned_data['end_time2']

        

        return HttpResponse("Timesheet successfully created.")
    else:
        form = SheetForm()

    return render(request, 'post.html', {
            'form': form,
    })


def submit(request, sheet_id):
    return HttpResponse("You have submitted the timesheet %s." %sheet_id)

def edit(request, sheet_id):
    return HttpResponse("You have edited the timesheet %s." %sheet_id)

def review(request, sheet_id):
    return HttpResponse("You have reviewed the timesheet %s." %sheet_id)

def approve(request, sheet_id):
    return HttpResponse("You have approved the timesheet %s." %sheet_id)

def decline(request, sheet_id):
    return HttpResponse("You have declined the timesheet %s." %sheet_id)
