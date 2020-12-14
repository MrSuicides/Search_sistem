from django.shortcuts import render, redirect
from .models import Product
from .forms import FormProduct
from django.views.generic import DetailView, DeleteView


def new_info(request):
    info = Product.objects.order_by('first_date')
    str_name = request.GET.get("name")
    if str(str_name) == 'None':
        return render(request, 'news/home.html', {'new': info})
    new = Product.objects.all().filter(statistical_weight=str_name)

    return render(request, 'news/home.html', {'new': new})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'news/details_view.html'
    context_object_name = 'product'


class ProductDelete(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'news/product-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = FormProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_info')
        else:
            error = 'Ошибка!!'
    form = FormProduct()

    info = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', info)
