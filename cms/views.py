from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Project
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from datetime import date
from datetime import datetime
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse, HttpResponseNotFound
import xlwt
from django.core.files.storage import FileSystemStorage
import pdfkit
from django.template.loader import get_template
import matplotlib
import random
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os,sys, stat
import matplotlib.image as mpimg






# Create your views here.
def barchart(request):
    objects=['a','b','c']
    y_pos=np.arrange(len(objects))
    qty=[10,20,25]
    plt.bar(y_pos,qty,align='enter',alpha=0.5)
    plt.xticks(y_pos,objects)
    plt.ylabel('quantity')
    plt.title('sales')
    plt.savefig('media/barchart.png')

def index(request):
    return render(request,"cms/index.html")

def login_view(request):
    all_projects=Project.objects.all()
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            all_projects=Project.objects.all()
            total_projects=0
            avg=0
            total_cost=0
            

            for project in all_projects:
                total_projects+=1
                total_cost+=project.cost
            
            avg=total_cost/total_projects
            return render(request, "cms/test2.html", {
                "all_projects": all_projects,"total_projects":total_projects,"cost":total_cost,"avg":avg
            })
        else:
            return render(request, "cms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cms/test2.html",{"all_projects": all_projects})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def mails(request):
    all_projects=Project.objects.all()
    # email alets:
    #for project in all_projects:
    #    if (project.enddate-datetime.date(datetime.now())).days <=10 and (project.enddate-datetime.date(datetime.now())).days > 0:
    #        send_mail(
    #            'Project Alert',
    #            'Project with SOD={sod} will expire on {enddate}'.format(sod=project.sod,enddate=project.enddate),
    #            'wavetecbusiness@gmail.com',
    #            [''],
    #                fail_silently=False,
    #                 )
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def form_view(request):
    if request.method=="POST":
        counter=0
        project=Project()
        project.projectname=request.POST["projectname"]
        project.name=request.POST["name"]
        project.email=request.POST["email"]
        project.sod=request.POST["sod"]
        #project.modules=request.POST["optradio"]
        if "first" in request.POST:
            project.webticket='True'
            counter+=1
        if "second" in request.POST:
            project.appointment='True'
            counter+=1
        if "third" in request.POST:
            project.watsapp='True'
            counter+=1
        project.region=request.POST.get("region")
        project.startdate=request.POST["startdate"]
        project.enddate=request.POST["enddate"]
        project.cost=request.POST["cost"]
        project.count=counter
        project.save()
        return render(request, "cms/confirmation.html",{
        "project":project
        })
    return HttpResponseRedirect(reverse("index"))



def dashboard(request):
    #all_projects=Project.objects.all()
    return render(request, "cms/login.html",
    
        #"all_projects":all_projects
    )


def project(request,item):
    project=Project.objects.get(id=item)

    return render(request, "cms/details.html",{
    "project":project
    })

def csv_export(request):
    all_projects=Project.objects.all()
    response=HttpResponse('')
    response['Content-Disposition']='attachment;filename=projects.csv'
    write=csv.writer(response)
    write.writerow(['Project Name','SOD','Modules','Cost','Region','StartDate','EndDate','Representative','Email'])
    projs=all_projects.values_list('projectname','sod','modules','cost','region','startdate','enddate','name','email')
    for proj in projs:
        write.writerow(proj)
    #in progress    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    students = [23,17,35,29,12]
    ax.pie(students, labels = langs,autopct='%1.2f%%')
    plt.savefig("cms/media/output.jpg")
    img1=mpimg.imread("cms/media/output.jpg")
    write.writerow(img1)
    ##
    return response

def excel_export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="projects.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Projects')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Project Name','SOD','Modules','Cost','Region','StartDate','EndDate','Representative','Email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    font_styledate = xlwt.XFStyle()
    font_styledate.num_format_str = 'dd/mm/yyyy'
    rows = Project.objects.all().values_list('projectname','sod','modules','cost','region','startdate','enddate','name','email')

    for row in rows:
        row_num += 1
        for col_num in range(5):
            ws.write(row_num, col_num, row[col_num], font_style)
        for col_num in range(5,9):
            ws.write(row_num, col_num, row[col_num], font_styledate)
   
    wb.save(response)
    return response




     
    





