from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForm
from service.models import service
from news.models import News
def userform(request):
    fn = userForm()
    data = {'form':fn}
    try:
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        finalans = n1+n2
        print(finalans)
        data = {
            'n1':n1,
            'n2':n2,
            'output':finalans,
            'form':fn
        }
        url = '/aboutus/?output={}'.format(finalans)
        return HttpResponseRedirect(url)
    except:
        pass  
    return render(request,'userform.html',data)
def marksheet(request):
    s1 = s2 = s3 = s4 = s5 = ''
    total=''
    per=''
    error = None
    if request.method == 'POST':
        s1 = request.POST.get('s1')
        s2 = request.POST.get('s2')
        s3 = request.POST.get('s3')
        s4 = request.POST.get('s4')
        s5 = request.POST.get('s5')

        
        if not s1 or not s2 or not s3 or not s4 or not s5:
            error = "All fields are required. Please fill in marks for all subjects."
        else:
                try:
                    
                    s1 = int(s1)
                    s2 = int(s2)
                    s3 = int(s3)
                    s4 = int(s4)
                    s5 = int(s5)

                    total = s1 + s2 + s3 + s4 + s5
                    per = round((total / 500) * 100) 
                except:
                    error = "enter numeric value"
    
    
    return render(request,'marksheet.html',{'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'total':total,'per':per,'error':error})
def even_odd(request):
    ans =""
    n1=''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            if n1 % 2 == 0:
                ans = " is even"
            else:
                ans = "is odd"
    except:
        ans = "invalid input"
    return render(request,'even_odd.html',{'ans':ans,'n1':n1}) 
def calculater(request):
    c=''
    n1 = ''
    n2='' 
    try:
        
        if request.method == 'POST':
            n1 = eval(request.POST['num1'])
            n2 = eval(request.POST['num2']) 
            opr = request.POST.get('operator')
            if opr == '+':
                c = n1+n2
            elif opr == '-':
                c = n1-n2
            elif opr == '*':
                c = n1*n2
            elif opr == '/':
                c = n1/n2
            else:
                print("invalid operator..!")
    except:
        c="invalid input...!"
        print(c)
        
    return render(request,'calculater.html',{'c':c,'n1':n1,'n2':n2}) 

def submitform(request):
    try:
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        finalans = n1+n2
        print(finalans)
        data = {
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
    except:
        pass
    return HttpResponse(finalans)
def aboutus(request):
    if request.method == 'GET':
        output=request.GET.get('output')
    return render(request,'aboutus.html',{'output':output})       
def course(request):
    return HttpResponse("welcome to course page....!")
def coursedetail(request,courseid):
    return HttpResponse(courseid)
def homepage(request):
    servicedata = service.objects.all().order_by('-service_icon')[:7]
    newsdata = News.objects.all()
    
    data = {
        'title':'Home Page',
        'bdata':'welcome to django templates',
        'clist': ['php','java','html'],
        'numbers':[10,20,30,40,50],
        'sdetails':[
            {'name':'pratap','phone':'9855548996'},
            {'name':'mehul','phone':'8956236598'}
        ],
        'servicedata':servicedata,
        'newsdata': newsdata,
        
        }
    
    return render(request,'index.html',data)
def news_detail(request,slug):
    print(slug)
    newsdata = News.objects.get(news_slug=slug)
    
    return render(request,'newsdetail.html',{'newsdata':newsdata})
def service_detail(request):
    
    servicedata = service.objects.all()
    if request.method == 'GET':
        st = request.GET.get('servicename')
        if st!= None:
           servicedata = service.objects.filter(service_title__icontains=st).values('service_desc') 
           
    
    return render(request,'servicedetail.html',{'servicedata':servicedata})