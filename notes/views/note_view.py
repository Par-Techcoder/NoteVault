from django.shortcuts import render, redirect
from notes.models import Note
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note(title=title, content=content).save()
        return redirect('note_list')

    return render(request, 'enduser/notes/create.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'enduser/notes/list.html', {'notes': notes})
