from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

@xframe_options_exempt
def index(request):
    return render(request, 'home/index.html')

def custom_404(request, exception):
    return render(request, '404.html')