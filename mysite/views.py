from django.shortcuts import render
def homePage(request):
    data={
        'title':'Home | Mywebsite'
    }
    return render(request,"index.html",data)

def interests(request):
    return render(request,"interest.html")

def contacts(request):
    return render(request,"contacts.html")

def gallery(request):
    return render(request,"gallery.html")