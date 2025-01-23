from django.shortcuts import render

# Create your views here.
def home (request):
    content = request.GET.POST()
    return render(request, 'home.html')
   