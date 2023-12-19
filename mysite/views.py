from django.shortcuts import render
def homePage(request):
    data={
        'title':'Home | Mywebsite',
        'mlist':['Ram','Hari','Krishna',"Bishnu"]
    }
    return render(request,"index.html",data)

def interests(request):
    return render(request,"interest.html")

def contacts(request):
    return render(request,"contacts.html")

def gallery(request):
    data={
        'numbers':[5,10,20,40,80,160],
        'details':[
        {'name':'Nabin Prasad Dhungana','phone':9863000000},
        {'name':'Prahari','phone':9843090901}]
    }
    return render(request,"gallery.html",data)