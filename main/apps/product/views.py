from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.views.generic import ListView, DetailView


from .models import Product
from apps.carts.models import Cart 

Pro = "product"  # short for Product App  ?-?-?

User = get_user_model()

# CLASS BASED VIEWS
class ProductListView(ListView):
    template_name = "product/product_landing.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/productDetail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_object = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context 

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug)
        if instance is None:
            raise Http404("Product not listed here!")
        return instance



# FUNCTION-BASED VIEWS

# def product_landing(request):
#     queryset = Product.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, 'product/product_landing.html', context)


def product_new(request):
    # forms instances
    # form = productForm(request.POST, request.FILES)
    form = productForm()
    cForm = CategoryModelForm(request.POST)

    context = {
        'form': form,
        'cForm': cForm,
    }

    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():

            print(form)
        return redirect('product:landing')
    else:
        return render(request, Pro + '/product_new.html', context)


def product_review(request):  # This should be merged with the product details.
    return render(request, Pro + '/product_review.html')


def editProduct(request):
    return render(request, Pro + '/editProduct.html')


def productDetail(request, product_id):
    print('Hello?')
    product = Product.objects.get(id=product_id)
    object = {
        'product': product,
    }
    return render(request, Pro + '/productDetail.html', object)



# POST or PUT routes for Products

# def updateProduct(request): # This will be the post for the update form
#     return render()

# def deleteProduct(request):
#     return render()
