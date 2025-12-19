from django.shortcuts import render
from Guest.models import*
from Builder.models import*
from User.models import *
from Admin.models import*

# Create your views here.
def HomePage(request):
    builderdata=tbl_builders.objects.get(id=request.session['bid'])
    return render(request,"Builder/HomePage.html",{'builders':builderdata})

def MyProfile(request):
    builderdata=tbl_builders.objects.get(id=request.session['bid'])
    return render(request,"Builder/MyProfile.html",{'builders':builderdata})

def EditProfile(request):
    builderdata=tbl_builders.objects.get(id=request.session['bid'])
    if request.method == "POST":
       name=request.POST.get("txt_name")
       email=request.POST.get("txt_email") 
       contact=request.POST.get("txt_contact")
       address=request.POST.get("txt_address")
       builderdata.builders_name=name
       builderdata.builders_email=email
       builderdata.builders_contact=contact
       builderdata.builders_address=address
       builderdata.save()
       return render(request,'Builder/EditProfile.html',{"msg":"Profile Updateed.."}) 
    else:
       return render(request,"Builder/EditProfile.html",{'builders':builderdata})

def ChangePassword(request):
    builderdata=tbl_builders.objects.get(id=request.session['bid'])
    builderpass=builderdata.builders_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if builderpass == oldpassword:
            if newpassword == repassword:
               builderdata.builders_password = newpassword
               builderdata.save()
               return render(request,"Builder/ChangePassword.html",{"msg":"Password Changed.."}) 
            else:
                return render(request,"Builder/ChangePassword.html",{"msg":"password Mismatch.."})
        else:
            return render(request,"Builder/ChangePassword.html",{"msg":"password Incorrect.."})
    else:
        return render(request,"Builder/ChangePassword.html",{'builders':builderdata})

def WorkerRegistration(request):
    workertypedata=tbl_workertype.objects.all()
    districtDatas=tbl_district.objects.all()
    if request.method =="POST":
        name =request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        builder=tbl_builders.objects.get(id=request.session['bid'])

        workertype=tbl_workertype.objects.get(id=request.POST.get("sel_workertype"))
        photo=request.FILES.get("file_photo")
        password=request.POST.get("txt_password")
        repassword=request.POST.get("txt_repassword")
        if password==repassword:
            tbl_worker.objects.create(worker_name=name,worker_email=email,workertype=workertype,worker_photo=photo,worker_password=password,place=place, worker_contact=contact,builder=builder)
            return render(request,"Builder/WorkerRegistration.html",{'msg':"Registration Successfully"})
        else:
            return render(request,"Builder/WorkerRegistration.html",{'msg':"password mismatch"})
    else:
        return render(request,'Builder/WorkerRegistration.html',{"districtDatas":districtDatas,"workertypedata":workertypedata})

def Work(request):
    workdata=tbl_work.objects.all()
    builder=tbl_builders.objects.get(id=request.session['bid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        details=request.POST.get("txt_details")
        photo=request.FILES.get("file_photo")
        tbl_work.objects.create(work_title=title,work_details=details,work_photo=photo,builder=builder)
        return render(request,'Builder/Work.html',{'msg':'Workadd successfully'})
    else:
        return render(request,'Builder/Work.html',{'workdata':workdata})

def DeleteWork(request,did):
    tbl_work.objects.get(id=did).delete()
    return render(request,'Builder/Work.html',{'msg':'Deleted successfully'})

def Gallery(request,id):
    gallerydata=tbl_workgallery.objects.all()
    if request.method=="POST":
        file=request.FILES.get("file_gallery")
        work=tbl_work.objects.get(id=id)
        tbl_workgallery.objects.create(work_file=file,work=work)
        return render(request,'Builder/Gallery.html',{'msg':'file inserted successfully'})
    else:
        return render(request,'Builder/Gallery.html',{'gallerydata':gallerydata})


def ViewRequest(request):
    viewreqdata=tbl_request.objects.filter(user_id=request.session['uid'])
    return render(request,'Builder/ViewRequest.html',{"viewreqdata":viewreqdata})

def Accept(request,aid):
    reqdata = tbl_request.objects.get(id=aid)
    reqdata.request_status=1
    reqdata.save()
    return render (request,'Builder/ViewRequest.html',{'msg':"Request Accepted..."})

def Reject(request,rid):
    reqdata = tbl_request.objects.get(id=rid)
    reqdata.request_status=2
    reqdata.save()
    return render (request,'Builder/ViewRequest.html',{'msg':"Request Rejected..."})

def ViewWorkers(request,rid):
    workertypedata=tbl_workertype.objects.all()
    viewworkersdata =tbl_worker.objects.all()
    requestdata=tbl_request.objects.get(id=rid)
    return render(request,'Builder/ViewWorkers.html',{"viewworkersdata":viewworkersdata,"workertypedata":workertypedata,'rid':rid })

def assign(request,wid,rid):
    viewworkersdata =tbl_worker.objects.get(id=wid)
    requestdata=tbl_request.objects.get(id=rid)
    tbl_assign.objects.create(request=requestdata,worker=viewworkersdata)
    return render(request,'Builder/ViewWorkers.html',{"wid":wid,"rid":rid,'msg':'Assigned Successfully..'})


def Amount(request,aid):
    reqdata = tbl_request.objects.get(id=aid)
    if request.method == "POST":
        amount=request.POST.get("txt_amount")
        reqdata.request_status=1
        reqdata.request_amount=amount
        reqdata.save()
        return render (request,'Builder/Amount.html',{'msg':'amount added successfully....'})
    else:
        return render (request,'Builder/Amount.html',{"reqdata":reqdata})

def Feedback(request):
    if request.method == "POST":
        builder=tbl_builders.objects.get(id=request.session['bid'])
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(feedback_content=content,builder=builder)
        return render (request,'Builder/Feedback.html',{'msg':'Successfully Inserted'})
    else:
        return render (request,'Builder/Feedback.html')