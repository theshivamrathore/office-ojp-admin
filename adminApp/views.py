from django.shortcuts import render
from django.http import HttpResponse
from GovtJobApp.models import *
# Create your views here.

def admin_login(request):
    if request.method=="POST":
        login = request.POST.get("loginid")
        pwd = request.POST.get("password")

        if login=='abc' and pwd=='abc':
            return render(request,'admin/panel.html')
        else:
            return HttpResponse("wrong id and password")
    return render (request,'admin/admin-panel.html')

def addjobs(request):
    if request.method=="POST":
        select = request.POST.get("select1")
        if select =="andamannicobar":
            pdate = request.POST.get("post_date")
            rboard = request.POST.get("recruitment_board")
            pname = request.POST.get("post_name")
            quali = request.POST.get("qualification")
            ano = request.POST.get("advt_no")
            ldate = request.POST.get("last_date")

            data = AndamanNicobarJobsModel(post_date=pdate,
                                    recruitment_board=rboard,
                                    post_name=pname,
                                    qualification=quali,
                                    advt_no=ano,
                                    last_date=ldate)
            data.save()

        elif select == "arunachalpradesh":
                pdate = request.POST.get("post_date")
                rboard = request.POST.get("recruitment_board")
                pname = request.POST.get("post_name")
                quali = request.POST.get("qualification")
                ano = request.POST.get("advt_no")
                ldate = request.POST.get("last_date")

                data = ArunachalPradeshJobsModel(post_date=pdate,
                                        recruitment_board=rboard,
                                        post_name=pname,
                                        qualification=quali,
                                        advt_no=ano,
                                        last_date=ldate)
                data.save()

    return render(request,'admin/addjobs.html')
