from django.shortcuts import render, redirect
from .forms import NewAnimalForm
from .models import Animal

# Create your views here.
def index(request):
    animals = Animal.objects.all()
    return render(request, 'shop_animals/shop.html', {'animals': animals})


def new_animal(request):
    if request.method == 'POST':
        form = NewAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewAnimalForm()
        return render(request, 'shop_animals/forms_add_animal.html', {'form': form})


