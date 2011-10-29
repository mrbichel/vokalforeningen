import datetime
from django.contrib.auth.views import redirect_to_login
from django.db.models.aggregates import Count
from models import Note, Category
from forms import NoteForm
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import list_detail, date_based, create_update
import settings

PAGINATE_BY = getattr(settings, 'PAGINATE_BY', 12)

def list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Note.objects.all(),
        paginate_by=PAGINATE_BY,
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

def create(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)

                note.author = request.user
                note.pub_date = datetime.datetime.now()

                note.save()

                return HttpResponseRedirect(note.get_absolute_url())
        else:
            form = NoteForm()

        return render(request, "corkboard/note_form.html", {'form': form})
    else:
        return redirect_to_login(request.path)


def update(request, id):
    note = Note.objects.get(id=id)
    if request.user == note.author:
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()

                return HttpResponseRedirect(note.get_absolute_url())
        else:
            form = NoteForm(instance=note)

        return render(request, "corkboard/note_form.html", {'form': form})
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