from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from Builder.models import*

# Create your views here.
def UserRegistration(request):
    districtDatas=tbl_district.objects.all()

    if request.method=="POST":
        photo=request.FILES.get("file_photo")
        name =request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        gender=request.POST.get("btn_gender")
        dob=request.POST.get("txt_DOB")
        district=request.POST.get("txt_district")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        password=request.POST.get("txt_password")
        repassword=request.POST.get("txt_repassword")

        
        if password==repassword:
            tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_gender=gender,user_dob=dob,user_photo=photo,user_password=password,place=place)
            return render(request,"Guest/UserRegistration.html",{'msg':"Registration Successfully"})
        else:
            return render(request,"Guest/UserRegistration.html",{'msg':"password mismatch"})
    else:
        return render(request,'Guest/UserRegistration.html',{'districtDatas':districtDatas})


def AjaxPlace(request):
    districtId=request.GET.get("did")
    place=tbl_place.objects.filter(district=districtId) 
    return render(request,"Guest/AjaxPlace.html",{'place':place})    

def Login(request):
    if request.method=="POST":
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_password')

        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        buildercount=tbl_builders.objects.filter(builders_email=email,builders_password=password).count()
        workercount=tbl_worker.objects.filter(worker_email=email,worker_password=password).count()

        if usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid'] =userdata.id
            return redirect("User:HomePage")
        elif admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] =admindata.id
            return redirect("Admin:HomePage")
        elif buildercount > 0:
            builderdata=tbl_builders.objects.get(builders_email=email,builders_password=password)
            request.session['bid'] =builderdata.id
            return redirect("Builder:HomePage")
        elif workercount > 0:
            workerdata=tbl_worker.objects.get(worker_email=email,worker_password=password)
            request.session['wid'] =workerdata.id
            return redirect("Worker:HomePage")            
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email or Password"})  
    else:
        return render(request,'Guest/Login.html')  

def BuilderRegistration(request):
    districtDatas=tbl_district.objects.all()
    
    if request.method =="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        district=request.POST.get("txt_district")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        logo=request.FILES.get("file_logo")
        license=request.FILES.get("file_license")
        password=request.POST.get("txt_password")
        repassword=request.POST.get("txt_repassword")


        if password==repassword:
            tbl_builders.objects.create(builders_name=name,builders_email=email,builders_contact=contact,builders_address=address,builders_logo=logo,builders_license=license,builders_password=password,place=place)
            return render(request,"Guest/BuilderRegistration.html",{"msg":"Registration successfully"})
        else:
            return render(request,"Guest/BuilderRegistration.html",{"msg":"password mismatch"}) 
    else:
        return render(request,"Guest/BuilderRegistration.html",{"districtDatas":districtDatas})







