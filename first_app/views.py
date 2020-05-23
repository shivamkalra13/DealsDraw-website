from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from first_app.models import User, Referal, Order, Offer, Product, Store
from first_app.serializers import UserSerializer, ReferalSerializer, OrderSerializer, OfferSerializer, ProductSerializer, StoreSerializer
from django.contrib.auth import hashers

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['password'] = hashers.make_password(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def user_auth(request):
    #Authenticate user using password using POST request\
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(phone = data['phone'])
        except User.DoesNotExist:
            return HttpResponse(status=404)
        if(hashers.check_password(data['password'],user.password)):#userinfo['password'] == user.password):
            #hash = hashers.make_password(user.password)
            #print(hashers.check_password(userinfo['password'],hash))
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data,status=201)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def referal_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        referals = Referal.objects.all()
        serializer = ReferalSerializer(referals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReferalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def referal_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        referal = Referal.objects.get(pk=pk)
    except Referal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReferalSerializer(referal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReferalSerializer(referal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        referal.delete()
        return HttpResponse(status=204)

@csrf_exempt
def order_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def order_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return HttpResponse(status=204)

@csrf_exempt
def offer_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def offer_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OfferSerializer(offer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(offer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        offer.delete()
        return HttpResponse(status=204)

@csrf_exempt
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=204)

@csrf_exempt
def store_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def store_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        store = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(store, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        store.delete()
        return HttpResponse(status=204)

#### Some Auxiliary functions

# def getNotes(sub,cls):
#     notesLst = list()
#     if(sub and cls):
#         subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
#         notesLst = Notes.objects.filter(subcode = subcode_selected)
#     elif(cls):
#         queryset = Subject.objects.filter(classno = cls)
#         for obj in queryset:
#             notesLst.extend(list(Notes.objects.filter(subcode = obj.subcode)))
#     else:
#         notesLst = Notes.objects.all()
#     return notesLst
#
# def getBooks(sub,cls):
#     booksLst = list()
#     if(sub and cls):
#         subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
#         booksLst = Books.objects.filter(subcode = subcode_selected)
#     elif(cls):
#         queryset = Subject.objects.filter(classno = cls)
#         for obj in queryset:
#             booksLst.extend(list(Books.objects.filter(subcode = obj.subcode)))
#     else:
#         booksLst = Books.objects.all()
#     return booksLst
#
# def getVideos(sub,cls):
#     videosLst = list()
#     if(sub and cls):
#         subcode_selected = (Subject.objects.filter(classno = cls).filter(subname = sub))[0].subcode
#         videosLst = Videos.objects.filter(subcode = subcode_selected)
#     elif(cls):
#         queryset = Subject.objects.filter(classno = cls)
#         for obj in queryset:
#             videosLst.extend(list(Videos.objects.filter(subcode = obj.subcode)))
#     else:
#         videosLst = Videos.objects.all()
#     return videosLst

##### Create your views here.
def index(request):
    offers = Offer.objects.all()
    mycontext={
        'offers': offers
    }
    return render(request, 'first_app/index.html', context=mycontext)

def classes(request):
    # GetParams = dict(request.GET)       #dictionary of GET parameters
    # sub_list = []                        #If no parameter is found then this empty list will pass
    # #class_list = Subject.objects.all().values('classno').distinct() #Get all distinct classno from db
    # class_list = Subject.class_names    #list of all the class names in Subject model
    # cld = None                          #If no parameter is found then this None will pass(selected class)
    # sbd = None                          #If no parameter is found then this None will pass(selected subject)
    # if(len(GetParams.keys())==1):       #Only class selected not subject
    #     cld = GetParams['cld'][0]          #getting classDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    # elif(len(GetParams.keys())==2):      #Both class and subject selected
    #     cld = GetParams['cld'][0]        #getting classDropdown parameter
    #     sbd = GetParams['sbd'][0]        #getting subjectDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    #
    # #getting the notes objects list according to the selected suject and class.
    # notes_lst = getNotes(sbd,cld)
    # books_lst = getBooks(sbd,cld)
    # videos_lst = getVideos(sbd,cld)
    #
    # mycontext={
    #     'sub_list':sub_list,     #List of subjects corresponding to classes
    #     'class_list':class_list,
    #     'sel_class':cld,
    #     'sel_sub':sbd,
    #     'notes_list':notes_lst,
    #     'books_list':books_lst,
    #     'videos_list':videos_lst
    # }
    return render(request, 'first_app/classes.html')#, context=mycontext)

def navbar(request):
    return render(request, 'first_app/navbar.html')

def notes(request):
    # GetParams = dict(request.GET)       #dictionary of GET parameters
    # sub_list = []                        #If no parameter is found then this empty list will pass
    # #class_list = Subject.objects.all().values('classno').distinct() #Get all distinct classno from db
    # class_list = Subject.class_names    #list of all the class names in Subject model
    # cld = None                          #If no parameter is found then this None will pass(selected class)
    # sbd = None                          #If no parameter is found then this None will pass(selected subject)
    # if(len(GetParams.keys())==1):       #Only class selected not subject
    #     cld = GetParams['cld'][0]          #getting classDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    # elif(len(GetParams.keys())==2):      #Both class and subject selected
    #     cld = GetParams['cld'][0]        #getting classDropdown parameter
    #     sbd = GetParams['sbd'][0]        #getting subjectDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    #
    # #getting the notes objects list according to the selected suject and class.
    # notes_lst = getNotes(sbd,cld)
    # books_lst = getBooks(sbd,cld)
    # videos_lst = getVideos(sbd,cld)
    #
    # mycontext={
    #     'sub_list':sub_list,     #List of subjects corresponding to classes
    #     'class_list':class_list,
    #     'sel_class':cld,
    #     'sel_sub':sbd,
    #     'notes_list':notes_lst,
    #     'books_list':books_lst,
    #     'videos_list':videos_lst
    # }
    return render(request, 'first_app/classes.html') #notes.html', context=mycontext)

def books(request):
    # GetParams = dict(request.GET)       #dictionary of GET parameters
    # sub_list = []                        #If no parameter is found then this empty list will pass
    # #class_list = Subject.objects.all().values('classno').distinct() #Get all distinct classno from db
    # class_list = Subject.class_names    #list of all the class names in Subject model
    # cld = None                          #If no parameter is found then this None will pass(selected class)
    # sbd = None                          #If no parameter is found then this None will pass(selected subject)
    # if(len(GetParams.keys())==1):       #Only class selected not subject
    #     cld = GetParams['cld'][0]          #getting classDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    # elif(len(GetParams.keys())==2):      #Both class and subject selected
    #     cld = GetParams['cld'][0]        #getting classDropdown parameter
    #     sbd = GetParams['sbd'][0]        #getting subjectDropdown parameter
    #     sub_list = Subject.objects.filter(classno = cld)
    #
    # #getting the notes objects list according to the selected suject and class.
    # notes_lst = getNotes(sbd,cld)
    # books_lst = getBooks(sbd,cld)
    # videos_lst = getVideos(sbd,cld)
    #
    # mycontext={
    #     'sub_list':sub_list,     #List of subjects corresponding to classes
    #     'class_list':class_list,
    #     'sel_class':cld,
    #     'sel_sub':sbd,
    #     'notes_list':notes_lst,
    #     'books_list':books_lst,
    #     'videos_list':videos_lst
    # }
    return render(request, 'first_app/classes.html') #books.html', context=mycontext)

def player(request):
    return render(request, 'first_app/videoplayer.html')
