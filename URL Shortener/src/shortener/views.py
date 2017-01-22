from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.http import HttpResponse
# Create your views here.
from .models import KirrURL
from .forms import SubmitUrlForm

def home_view_fbv(request, *args, **kwargs):
    if(request.method == "POST"):
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Mantis",
            "form" : the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "Mantis",
            "form" : form
        }
        if(form.is_valid()):
            print(form.cleaned_data)
        return render(request, "shortener/home.html", context)

class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
        #return HttpResponse("Hello again {sc}".format(sc=obj.url))
