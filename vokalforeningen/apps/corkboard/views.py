from __future__ import unicode_literals
import datetime
import pprint
from django.contrib.auth.views import redirect_to_login
from django.db.models.aggregates import Count
from django.template import Context
from models import Note, Category
from forms import NoteForm, TimeForm
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail, date_based, create_update
from django.conf import settings
PAGINATE_BY = getattr(settings, 'PAGINATE_BY', 12)


def event_list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Note.objects.filter(is_event=True, end__gte=datetime.datetime.now()-datetime.timedelta(days=1)).order_by('start'),
        paginate_by=PAGINATE_BY,
        extra_context={'listtitle': 'Events'},
        **kwargs
    )

def note_list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Note.objects.filter(is_event=False).order_by('-pub_date'),
        paginate_by=PAGINATE_BY,
        extra_context={'listtitle': 'Opslag'},
        **kwargs
    )

def detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, "corkboard/note_detail.html", {'object': note})

def by_category(request, slug, **kwargs):
    cat = get_object_or_404(Category, slug=slug)
    return list_detail.object_list(
        request,
        queryset=Note.objects.filter(category=cat),
        paginate_by=PAGINATE_BY,
        **kwargs
    )

def create(request, event):
    if request.user.is_authenticated():
        c = Context()
        if request.method == 'POST':
            form = NoteForm(request.POST)
            if event:
                timeform = TimeForm(request.POST)
                c.update({'timeform': timeform})

            if form.is_valid():
                note = form.save(commit=False)
                note.author = request.user
                note.pub_date = datetime.datetime.now()

                if not event:
                    note.save()
                    return HttpResponseRedirect(note.get_absolute_url())

                else:
                    #pprint.pprint(timeform.data)

                    if timeform.is_valid():
                        #pprint.pprint(timeform.cleaned_data)

                        note.end = datetime.datetime.combine(
                                timeform.cleaned_data['end_date'],
                                timeform.cleaned_data['end_time']
                            )

                        note.start = datetime.datetime.combine(
                                timeform.cleaned_data['start_date'],
                                timeform.cleaned_data['start_time']
                            )

                        note.is_event = True
                        note.save()
                        return HttpResponseRedirect(note.get_absolute_url())
                    
        else:
            form = NoteForm()
            if event:
                c.update({'timeform': TimeForm()})

        c.update({'form': form, 'is_event': event})
        return render(request, "corkboard/note_form.html", c)
    else:
        return redirect_to_login(request.path)


def update(request, id):
    note = Note.objects.get(id=id)

    if request.user == note.author:
        c = Context({'object': note})
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if note.is_event:
                timeform = TimeForm(request.POST)
                c.update({'timeform': timeform})

            if form.is_valid():
                if not note.is_event:
                    note.save()
                    return HttpResponseRedirect(note.get_absolute_url())

                else:
                    if timeform.is_valid():
                        pprint.pprint(timeform.cleaned_data)

                        note.end = datetime.datetime.combine(
                                timeform.cleaned_data['end_date'],
                                timeform.cleaned_data['end_time']
                            )

                        note.start = datetime.datetime.combine(
                                timeform.cleaned_data['start_date'],
                                timeform.cleaned_data['start_time']
                            )

                        note.save()
                        return HttpResponseRedirect(note.get_absolute_url())
        else:
            form = NoteForm(instance=note)
            if note.is_event:
                c.update({'timeform': TimeForm({
                    'start_date': note.start.date(),
                    'start_time': note.start.time(),
                    'end_date': note.end.date(),
                    'end_time': note.end.time(),
                    })
                })

        c.update({'form': form, 'is_event': note.is_event})
        return render(request, "corkboard/note_form.html", c)
    else:
        return HttpResponseForbidden("Du har ikke tilladelse til at redigere dette opslag.")

def delete(request, id):
    note = Note.objects.get(id=id)
    if request.user == note.author:

        return create_update.delete_object(
            request,
            login_required=True,
            model=Note,
            object_id=id,
            post_delete_redirect="/",
        )

    else:
        return HttpResponseForbidden("Du har ikke tilladelse til at slette dette opslag.")