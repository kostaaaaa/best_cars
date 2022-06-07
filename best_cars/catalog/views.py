from django.shortcuts import redirect, render
from .models import Brand, CarModel
from .forms import AddCarForm


def index(request):
    catalog = CarModel.objects.all()
    return render(request, 'index.html', {'catalog': catalog})


def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)
        if form.is_valid():
            brand1 = request.POST['brand']
            brand = Brand.objects.filter(name=brand1).first()
            model = form.cleaned_data['model']
            engine_type = form.cleaned_data['engine_type']
            engine_capacity = form.cleaned_data['engine_capacity']
            body_type = form.cleaned_data['body_type']
            power = form.cleaned_data['power']
            year = form.cleaned_data['year']
            CarModel.objects.create(
                brand=brand, 
                model=model, 
                engine_type=engine_type,
                engine_capacity=engine_capacity,
                body_type=body_type,
                power=power,
                year=year
            )
            return redirect('/')
    else:
        form = AddCarForm()
    
    return render(request, 'add.html', {'form': form})
