from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import UserForm

def homePage(request):
    data={
        'title':'Home | Mywebsite',
        'mlist':['Ram','Hari','Krishna',"Bishnu"]
    }
    return render(request,"index.html",data)

def interests(request):
    # if request.method=="GET":
    #     output=request.GET.get('output')
    return render(request,"interest.html")#,{output})

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

def userform(request):
    ans=0
    fn=UserForm()
    data={'form': fn}
    try:
        if request.method=="POST":
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            ans=n1+n2
            data={'form': fn,
                'n1':n1,
                  'n2':n2,
                  'output':ans
                  }
            
            url="thank-you/?output={}".format(ans)
            return HttpResponseRedirect(url)
    except:
        print("Invalid")
    return render(request,"userform.html",data)

def submitform(request):
    ans=0
    data={}
    try:
        if request.method=="POST":
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            ans=n1+n2
            data={'n1':n1,
                  'n2':n2,
                  'output':ans
                  }
            
            url="thank-you/?output={}".format(ans)
            return HttpResponseRedirect(url)
    except:
        print("Invalid")
    
def thankyou(request):
    return render(request,'thankyou.html')