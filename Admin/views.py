from django.shortcuts import render
from Admin.models import *
from Guest.models import *
from User.models import *
from Builder.models import *

# Create your views here.
def District(request):
    districtDatas=tbl_district.objects.all()
    if request.method=="POST":
       districtname=request.POST.get('txt_districtname')
       checkdistrict=tbl_district.objects.filter(district_name=districtname).count()
       if checkdistrict > 0:
           return render(request,'Admin/District.html',{'msg':'District Already Existed '})
       else:
            tbl_district.objects.create(district_name=districtname)
            return render(request,'Admin/District.html',{'msg':'Inserted successfully'})
    else:
        return render(request,'Admin/District.html',{'districtDatas':districtDatas})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':'Deleted successfully'}) 
def EditDistrict(request,eid):
    districtOne=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        checkdistrict=tbl_district.objects.filter(district_name=request.POST.get("txt_districtname")).count()
        if checkdistrict > 0:
           return render(request,'Admin/District.html',{'msg':'District Already Existed '})
        else:
            districtOne.district_name=request.POST.get("txt_districtname")
            districtOne.save()
            return render(request,'Admin/District.html',{'msg':'Edited successfully'})
    else:
        return render(request,'Admin/District.html',{'districtOne':districtOne})   


def Category(request):
    categoryDatas=tbl_category.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get('txt_categoryname')
        tbl_category.objects.create(category_name=categoryname)
        return render(request,'Admin/Category.html',{'msg':'Inserted successfully'})
    else:
        return render(request,'Admin/Category.html',{'categoryDatas':categoryDatas}) 
def DeleteCategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Admin/Category.html',{'msg':'Deleted successfully'})       
    
def EditCategory(request,eid):
    CategoryOne=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        CategoryOne.category_name=request.POST.get("txt_categoryname")
        CategoryOne.save()
        return render(request,'Admin/Category.html',{'msg':'Edited successfully'})
    else:
        return render(request,'Admin/Category.html',{'CategoryOne':CategoryOne})   


def  Place(request):
    districtDatas=tbl_district.objects.all()
    placeDatas=tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placename=request.POST.get('txt_placename')
        tbl_place.objects.create(place_name=placename,district=district)
        return render(request,'Admin/Place.html',{'msg':"Inserted successfully"})
    else:
      return render(request,'Admin/Place.html',{'districtDatas':districtDatas,'placeDatas':placeDatas})  

def DeletePlace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return render(request,'Admin/Place.html',{'msg':'Deleted successfully'})

def EditPlace(request,eid):
    districtDatas=tbl_district.objects.all()
    placeOne=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placeOne.place_name=request.POST.get("txt_placename")
        placeOne.district = district
        placeOne.save()
        return render(request,'Admin/place.html',{'msg':'Edited successfully'})
    else:
        return render(request,'Admin/place.html',{'placeOne':placeOne,'districtDatas':districtDatas}) 


def Subcategory(request):
    categoryDatas=tbl_category.objects.all()
    subcategoryDatas=tbl_subcategory.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryname=request.POST.get('txt_subcategory') 
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=category) 
        return render(request,'Admin/Subcategory.html',{'msg':"Inserted successfully"})
    else:
        return render(request,'Admin/Subcategory.html',{'categoryDatas':categoryDatas,'subcategoryDatas':subcategoryDatas})

def DeleteSubcategory(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return render(request,'Admin/Subcategory.html',{'msg':'Deleted successfully'})

def EditSubcategory(request,eid):
    categoryDatas=tbl_category.objects.all()
    subcategoryOne=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryOne.subcategory_name=request.POST.get("txt_subcategory")
        subcategoryOne.category=category
        subcategoryOne.save()
        return render(request,'Admin/Subcategory.html',{'msg':'Edited successfully'})
    else:
        return render(request,'Admin/Subcategory.html',{'subcategoryOne':subcategoryOne,'categoryDatas':categoryDatas}) 



def AdminRegistration(request):
    adminDatas=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        checkadminregistration=tbl_admin.objects.filter(admin_email=email).count()
        if checkadminregistration > 0:
           return render(request,'Admin/AdminRegistration.html',{'msg':'Email is Already Existed '})
        else:
           tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
           return render(request,"Admin/AdminRegistration.html",{'msg':'Inserted successfully' })
    else:
        return render(request,"Admin/AdminRegistration.html",{"adminDatas":adminDatas})
def DeleteAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,'Admin/AdminRegistration.html',{'msg':'Deleted successfully'})

def UserList(request):
    userdata=tbl_user.objects.all()
    return render(request,'Admin/UserList.html',{"userdata":userdata})    

def ViewComplaint(request):
    complaintdata= tbl_complaint.objects.filter(Complaint_status=0)
    complaintone=tbl_complaint.objects.filter(Complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{"complaintdata":complaintdata,"complaintone":complaintone})

def Reply(request,eid):
    complaintone=tbl_complaint.objects.get(id=eid)
    if request.method =="POST":
        complaintone.Complaint_reply=request.POST.get("txt_reply")
        complaintone.Complaint_status=1
        complaintone.save()
        return render(request,'Admin/Reply.html',{'msg':'Replied Successfully...'})
    else:
       return render(request,'Admin/Reply.html',{"complaintone":complaintone})

def WorkType(request):
    worktypedata=tbl_worktype.objects.all()
    if request.method=="POST":
        worktype=request.POST.get("txt_worktype")
        checkworktype=tbl_worktype.objects.filter(worktype_name=worktype).count()
        if checkworktype > 0:
           return render(request,'Admin/WorkType.html',{'msg':'worktype is Already Existed '})
        else:

            tbl_worktype.objects.create(worktype_name=worktype)
            return render(request,'Admin/WorkType.html',{'msg':'inserted successfully'})
    else:
        return render(request,'Admin/WorkType.html',{"worktypedata":worktypedata})

def DeleteWorktype(request,did):
    tbl_worktype.objects.get(id=did).delete()
    return render(request,'Admin/WorkType.html',{'msg':'Deleted successfully'})

def WorkerType(request):
    workertypedata=tbl_workertype.objects.all()
    if request.method == "POST":
        workertype=request.POST.get("txt_workertype")
        checkworkertype=tbl_workertype.objects.filter(workertype_name=workertype).count()
        if checkworkertype > 0:
           return render(request,'Admin/WorkerType.html',{'msg':'WorkerType Already Existed '})
        else:
            tbl_workertype.objects.create(workertype_name=workertype)
            return render(request,'Admin/WorkerType.html',{'msg':'inserted successfully'})
    else:
        return render(request,'Admin/WorkerType.html',{"workertypedata":workertypedata})

def BuildersVerification(request):
    buildersverificationdata=tbl_builders.objects.all()
    return render(request,'Admin/BuildersVerification.html',{"buildersverificationdata":buildersverificationdata})    

def Accept(request,aid):
    buildersverificationdata = tbl_builders.objects.get(id=aid)
    buildersverificationdata.request_status=1
    buildersverificationdata.save()
    return render (request,'Admin/BuildersVerification.html',{'msg':"Request Accepted..."})

def Reject(request,rid):
    buildersverificationdata = tbl_builders.objects.get(id=rid)
    buildersverificationdata.request_status=2
    buildersverificationdata.save()
    return render (request,'Admin/BuildersVerification.html',{'msg':"Request Rejected..."})

def Feedback(request):
    user=tbl_user.objects.all()
    userfeedback=tbl_feedback.objects.filter(user__in=user)
    builder=tbl_builders.objects.all()
    builderfeedback=tbl_feedback.objects.filter(builder__in=builder)
    worker=tbl_worker.objects.all()
    workerfeedback=tbl_feedback.objects.filter(worker__in=worker)
    return render(request,'Admin/Feedback.html',{'userfeedback':userfeedback,'builderfeedback':builderfeedback,'workerfeedback':workerfeedback})


def HomePage(request):
    admindata=tbl_admin.objects.get(id=request.session['aid'])
    user = tbl_user.objects.all().count()
    builder=tbl_builders.objects.all().count()
    worker=tbl_worker.objects.all().count()
    return render(request,"Admin/HomePage.html",{' admindata': admindata,'userdata':user,'builderdata':builder,'workerdata':worker})



    