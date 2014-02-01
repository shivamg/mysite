
from dobby.models import Product
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dobby.serializers import ProductSerializer


def search_form(request):

    return render(request, 'dobby/search.html')


def index(request):
    #user = authenticate(username=username, password=password)
    #assert isinstance(user, mongoengine.django.auth.User)

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        product_list = SearchQuerySet().filter(content=q)
        #product_list = Product.objects.filter(name__icontains=q)
        latest_product_list = product_list[:5]
        return render_to_response('dobby/haystack_index.html', {'products': latest_product_list},
                              context_instance=RequestContext(request))
    else:
        return HttpResponse('Please submit a search term.')


# Django Rest Framework related code
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def product_list(request):
    """
    List all code products, or create a new products.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def product_detail(request, pk):

    #Retrieve, update or delete a code snippet.

    try:
        product = Product.objects.get(prodid=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)