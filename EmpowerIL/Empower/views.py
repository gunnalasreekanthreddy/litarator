from django.shortcuts import render

# Create your views here.
def home(request):
    # cat = category.objects.all()
    if request.POST.get('home'):
        return render(request, 'homepanel.html')
    #     catg = request.POST.get('category')
    #     ca = catg.lower()
    #     for c in cat:
    #         if ca == c.bcategory:
    #             msg = 'category already exist'
    #             return render(request, 'addcategoey.html', {'categories': cat, 'msg': msg})
    #     category.objects.create(bcategory=catg)
    #     cat = category.objects.all()
    #     msg = 'succesfully category added'
    elif request.POST.get('hiree'):
          return render(request, 'hiree.html')
    elif request.POST.get('hirer'):
        return render(request,'hirer.html')
    else:
        return render(request, 'Home.html')
def Update(request):
    if request.POST:
         return render(request,'upadate.html')
    else:
        return render(request, 'update.html')