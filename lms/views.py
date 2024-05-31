from django.shortcuts import render, redirect
from .models import Course, Note
from .forms import NoteForm
from django.contrib import messages


def courseview(request):
    courses = Course.objects.all().order_by('-id')
    context ={'courses':courses}
    return render(request, 'lms/courses.html', context)

def note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            fform = form.save(commit=False)
            fform.user = request.user
            fform.save()
            messages.success(request, 'Note added. ')
            return redirect('lms:notes')
    form = NoteForm
    current_user = request.user
    notes = Note.objects.filter(user=current_user)
    context = {'form':form, 'notes':notes}
    return render(request, 'lms/note.html', context)

def note_detail(request, nid):
    note = Note.objects.get(id=nid)
    context = {'note':note}
    return render(request,'lms/note-detail.html', context)

def note_update(request, nid):
    note = Note.objects.get(id=nid)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated')
            return redirect('lms:note-update', nid=form.instance.id )

    

    context = {'form':form}
    return render(request,'lms/note-update.html', context)

def note_delete(request,nid):
    note= Note.objects.get(id=nid)
    note.delete()
    messages.success(request,'Note Deleted.')
    return redirect('lms:notes')