from django.shortcuts import render

def index(request):
    template_name = 'base.html'
    context = {
        'core': 'core',
    }
    return render(request, template_name, context)
