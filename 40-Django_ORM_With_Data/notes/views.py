from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')  # Replace 'home' with your actual home view name
    else:
        form = NoteForm()

    return render(request, 'create_note.html', {'form': form})


def view_edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')  # Replace 'home' with your actual home view name
    else:
        form = NoteForm(instance=note)

    return render(request, 'view_edit_note.html', {'form': form, 'note': note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes')  # Replace 'home' with your actual home view name
