from django.shortcuts import render
from .models import Memo

# Create your views here.

def index (request) :

    memos = Memo.objects.all()

    context = {
        'name': '장고',
        'memos': memos
    }

    return render(request=request, template_name='polls/index.html', context=context)
