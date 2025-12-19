from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from Builder.models import*
from Worker.models import*
from django.http import JsonResponse

# Create your views here.
def HomePage(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/HomePage.html",{'user':userdata})

def MyProfile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'user':userdata})

def EditProfile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
       name=request.POST.get("txt_name")
       email=request.POST.get("txt_email") 
       contact=request.POST.get("txt_contact")
       address=request.POST.get("txt_address")
       userdata.user_name=name
       userdata.user_email=email
       userdata.user_contact=contact
       userdata.user_address=address
       userdata.save()
       return render(request,'User/EditProfile.html',{"msg":"Profile Updateed.."}) 
    else:
       return render(request,"User/EditProfile.html",{'user':userdata})

def ChangePassword(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    userpass=userdata.user_password
    if request.method == "POST":
        oldpassword=request.POST.get("txt_oldpassword")
        newpassword=request.POST.get("txt_newpassword")
        repassword=request.POST.get("txt_repassword")
        if userpass == oldpassword:
            if newpassword == repassword:
                userdata.user_password = newpassword
                userdata.save()
                return render(request,"User/ChangePassword.html",{"msg":"Password Changed.."}) 
            else:
                return render(request,"User/ChangePassword.html",{"msg":"password Mismatch.."})
        else:
            return render(request,"User/ChangePassword.html",{"msg":"password Incorrect.."})
    else:
        return render(request,"User/ChangePassword.html",{'user':userdata})

def Complaint(request):
    complaintdata=tbl_complaint.objects.filter(user_id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(Complaint_title=title,Complaint_content=content,user_id=user)
        return render(request,'User/Complaint.html',{"msg":'complaint registered..'})    
    else:
        return render(request,'User/Complaint.html',{ "complaintdata": complaintdata})   


def DeleteComplaint(request,cid):
    tbl_complaint.objects.get(id=cid).delete()
    return render(request,'User/Complaint.html',{'msg':'Deleted successfully..'})

def ViewBuilders(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    viewdata=tbl_builders.objects.filter(id=request.session['bid'])
    tot=0
    for i in viewdata:
        ratecount=tbl_rating.objects.filter(builder=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(builder=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(viewdata,parry)
    return render(request,'User/ViewBuilders.html',{"viewdata":datas,'ar':ar})   

def ViewWork(request,id):
    viewworkdata=tbl_work.objects.filter(builder=id)
    return render(request,'User/ViewWork.html',{"viewworkdata":viewworkdata})

def ViewGallery(request,id):
    gallerydata=tbl_workgallery.objects.all()
    if request.method=="POST":
        file=request.FILES.get("file_gallery")
        work=tbl_work.objects.get(id=id)
        tbl_workgallery.objects.create(work_file=file,work=work)
        return render(request,'User/ViewGallery.html',{'msg':'file inserted successfully'})
    else:
        return render(request,'User/ViewGallery.html',{'gallerydata':gallerydata})

def Request(request,id):
    if request.method=="POST":
        content=request.POST.get("txt_content")
        file=request.FILES.get("file_photo")
        builderid=tbl_builders.objects.get(id=id)
        userid=tbl_user.objects.get(id=request.session['uid'])
        tbl_request.objects.create(request_content=content,request_file=file,builder=builderid,user=userid)
        return render(request,'User/Request.html',{'msg':'request successfully'})
    else:
        return render(request,'User/Request.html')

def MyRequest(request):
    reqdata=tbl_request.objects.filter(user_id=request.session['uid'])
    return render (request,"User/MyRequest.html",{"reqdata":reqdata})

def Accept(request,aid):
    reqdata = tbl_request.objects.get(id=aid)
    reqdata.request_status=3
    reqdata.save()
    return render (request,"User/MyRequest.html",{'msg':'Accept successfully..'})

def Reject(request,rid):
    reqdata = tbl_request.objects.get(id=rid)
    reqdata.request_status=4
    reqdata.save()
    return render (request,"User/MyRequest.html",{'msg':'Reject successfully..'})

def ViewUpdate(request,id):
    updatedata=tbl_updates.objects.all()
    return render (request,"User/ViewUpdate.html",{'updatedata':updatedata})

def Feedback(request):
    if request.method == "POST":
        user=tbl_user.objects.get(id=request.session['uid'])
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(feedback_content=content,user=user)
        return render (request,'User/Feedback.html',{'msg':'Successfully Inserted'})
    else:
        return render (request,'User/Feedback.html')












  






 




def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(builder=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(builder=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user = tbl_user.objects.get(id=request.session['uid'])
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=user,user_review=user_review,rating_data=rating_data,builder=tbl_builders.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(builder=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(builder=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(builder=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)




def Payment(request,rid):
    reqdata=tbl_request.objects.get(id=rid)
    amount=int(reqdata.request_amount) / 2 
    if request.method == "POST":
        reqdata.request_status = 5 
        reqdata.save()
        return redirect("User:Loader")
    else:
        return render(request,"User/Payment.html",{'amount':amount})
def Loader(request):
    return render(request,"User/Loader.html")

def Payment_suc(request):
    return render(request,"User/Payment_suc.html")