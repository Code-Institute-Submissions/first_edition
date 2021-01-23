from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from django.template import loader
from checkout.forms import RateForm
from checkout.models import Review, ReviewForm, OrderLineItem, Rating
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        'current_categories': categories,
        'current_sorting': current_sorting,

        }

    return render(request, "products/products.html", context)


def product_bestsellers(request):

    product_bestsellers = Product.objects.filter(is_bestseller=True)

    context = {
        "product_bestsellers": product_bestsellers,
        }

    return render(request, "products/product_bestsellers.html", context)


def product_detail(request, product_id):
    """ A view to show a single product details """

    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product_id)
    is_buyer = False
    lines = OrderLineItem.objects.filter(product=product)
    rating = Rating.objects.filter(product=product_id)
    for line in lines:
        order = line.order
        if order.user_profile == request.user.userprofile:
            is_buyer = True

    context = {
        "product": product,
        "review": review,
        "is_buyer": is_buyer,
        "rating": rating,
        }
    return render(request, "products/product_detail.html", context)


def view_comments(request, product_id):
    reviews = Review.objects.filter(product=product_id)
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "reviews": reviews,
        "product": product,
    }
    return render(request, "products/reviews.html", context)



def add_comment(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            data = form.save()
            data.product_id = product_id
            data.user = profile
            data.save()
            messages.success(request, 'Your review has been posted.')
            return HttpResponseRedirect(url)
        else:
            messages.error(request, "error in making this review")

    return HttpResponseRedirect(url)


def edit_comment(request, product_id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product_id)
    user_session = UserProfile.objects.get(user=request.user)
    print("review")

    return HttpResponseRedirect(url)


def delete_comment(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def rate(request, product_id):

    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            rate = form.save(commit=False)
            rate.user = profile
            rate.produt = product
            rate.save()
            messages.success(
                request, 'You have successfully rated this product.')
            return redirect(
                reverse('product_detail', args=[product_id]))
        else:
            form = RateForm()

    template = loader.get_template('products/product_detail.html')

    context = {
        'form': form,
        'product': product,
        }

    return HttpResponse(template.render(context, request))


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, "Failed to add product."
                "Please ensure the form is valid.")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product"
                "Please ensure the form is valid.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
