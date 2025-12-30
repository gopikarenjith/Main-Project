from django.shortcuts import render,redirect
from Builder.models import*
from Worker.models import*

# Create your views here.
def HomePage(request):
    workerdata=tbl_worker.objects.get(id=request.session['wid'])
    return render(request,"Worker/HomePage.html",{'worker':workerdata})

def MyProfile(request):
    workerdata=tbl_worker.objects.get(id=request.session['wid'])
    return render(request,"Worker/MyProfile.html",{'worker':workerdata})

def EditProfile(request):
    workerdata=tbl_worker.objects.get(id=request.session['wid'])
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        checkprofile=tbl_worker.objects.filter(worker_email=email).count()
        if checkprofile > 0:
            return render(request,'User/EditProfile.html',{'msg':'Email Already Existed '})
        else:
        
            workerdata.worker_name=name
            workerdata.worker_email=email
            workerdata.worker_contact=contact
            workerdata.save()
            return render(request,'Worker/EditProfile.html',{"msg":"Profile Updateed.."}) 
    else:
       return render(request,"Worker/EditProfile.html",{'worker':workerdata})
 
def ChangePassword(request):
    workerdata=tbl_worker.objects.get(id=request.session['wid'])
    workerpass=workerdata.worker_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if workerpass == oldpassword:
            if newpassword == repassword:
                workerdata.worker_password = newpassword
                workerdata.save()
                return render(request,"Worker/ChangePassword.html",{"msg":"Password Changed.."}) 
            else:
                return render(request,"Worker/ChangePassword.html",{"msg":"password Mismatch.."})
        else:
            return render(request,"Worker/ChangePassword.html",{"msg":"password Incorrect.."})
    else:
        return render(request,"Worker/ChangePassword.html",{'workerdata':workerdata})



def ViewAssign(request):
    assigndata=tbl_assign.objects.filter(worker=request.session['wid'])
    return render(request,'Worker/ViewAssign.html',{"assigndata":assigndata})

def UpdateAssign(request,id,status):
    assign = tbl_assign.objects.get(id=id)
    assign.assign_status=status
    assign.save()
    if status== 1:
        msg="Started Successfully"
    elif status == 2:
        msg="Ended Successfully"
    return render(request,'Worker/ViewAssign.html',{'msg':msg})

def Updates(request,id):
    updatesdate=tbl_updates.objects.all()
    assigndata=tbl_assign.objects.get(id=id)
    if request.method=="POST":
        content=request.POST.get("txt_content")
        tbl_updates.objects.create(updates_content=content,assign=assigndata)
        return render (request,'Worker/Updates.html',{"msg":"updates successfully"})
    else:
        return render (request,'Worker/Updates.html',{"updatesdate":updatesdate})

def Feedback(request):
    if request.method == "POST":
        worker=tbl_worker.objects.get(id=request.session['wid'])
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(feedback_content=content,worker=worker)
        return render (request,'Worker/Feedback.html',{'msg':'Successfully Inserted'})
    else:
        return render (request,'Worker/Feedback.html')



def Logout(request):
    del request.session['wid']
    return redirect('Guest:Login')
