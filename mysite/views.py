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
    try:
        if request.method=='POST':
            url='/?submitted'
            return HttpResponseRedirect(url)
    except:
        print('Invalid')
    return render(request,'thankyou.html')

def calculator(request):
    data={}
    try:
        if request.method=='POST':
            n1=request.POST.get('num1')
            n2=request.POST.get('num2')
            opr=request.POST.get('opr')
            match opr:
                case '+':
                    result=int(n1)+int(n2)
                    
                case '-':
                    result=int(n1)-int(n2)

                case '*':
                    result=int(n1)*int(n2)

                case '/':
                    try:
                        result=float(n1)/float(n2)

                    except:
                        result='Error! Division by zero is not allowed.'

            data={'num1': n1,
                'num2':n2,
                  'result':result
                  }
    except:
        pass
    return render(request,"calculator.html",data)

def evenodd(request):
    data={}
    result=''
    num=0
    try:
        if request.method=='POST':
            num=int(request.POST.get('num'))
            if(num%2==0):
                result="Even"
            else:
                result="Odd"   

    except:
        result='Invalid input'
    
    data={'number':num, 'result':result}
    return render(request,'evenodd.html',data)

def marksheet(request):
    # subjects=['mark1','mark2','mark3','mark4','mark5','mark6']
    remarks=''
    total=0
    percent=0
    division=''
    count=0
    result=''
    data={}
    mark1=int(request.POST.get('mark1'))
    mark2=int(request.POST.get('mark2'))
    mark3=int(request.POST.get('mark3'))
    mark4=int(request.POST.get('mark4'))
    mark5=int(request.POST.get('mark5'))
    mark6=int(request.POST.get('mark6'))
    try:
        if request.method=='POST':
            subjects=[mark1,mark2,mark3,mark4,mark5,mark6]
            for sub in subjects:
                try:
                    if(sub>=0 and sub<=100):
                        total=total+sub
                    remarks="Everything's Okay"
                except:
                    remarks='Marks must be between 0 to 100!'
                if(sub<40):
                    count+=1

        percent=(total/6)
        if(percent>=80):
            division='Distinction'
        elif(percent>=60):
            division='First Division'
        elif(percent>=50):
            division='Second Division'
        else:
            division='Third Division'

        if(count!=0):
            result='Fail'
        else:
            result='Pass'
        

    except:
        pass

    data={'mark1':mark1,'mark2':mark2,'mark3':mark3,'mark4':mark4,'mark5':mark5,'mark6':mark6,'total':total,'percent':percent,'division':division,'result':result,'remarks':remarks}
    

    return render(request,'marksheet.html',data)