from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms.forms import name
# Create your views here.
def index(request):
  return render(request, 'index.html')


def signup(request):
    # if this is a POST request we need to process the form data
    form  = name()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = name(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save(commit=True)
            return index(request)

    # if a GET (or any other method) we'll create a blank form
    else:
        print("invalid form")

    return render(request, 'signup.html', {'form': form})

