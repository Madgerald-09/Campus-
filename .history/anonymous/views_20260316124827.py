from django.shortcuts import render, redirect
from .models import Confession

def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Confession.objects.create(text=text)
        return redirect('index')
    
    confessions = Confession.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'confessions': confessions})