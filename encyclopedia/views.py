from django.shortcuts import render, redirect
from .forms import WikiForm

from . import util


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def create(request):
    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return redirect('view', title=title)
        
    else:
        form = WikiForm()


    return render(request, 'encyclopedia/create.html', {'form': form})

def view(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, '404.html')
    else:
        return render(request, 'encyclopedia/view.html', {'title': title, 'content': content})


