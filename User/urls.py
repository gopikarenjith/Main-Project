from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('HomePage/',views.HomePage, name="HomePage"),
    path('MyProfile/',views.MyProfile, name="MyProfile"),
    path('EditProfile/',views.EditProfile, name="EditProfile"),
    path('ChangePassword/',views.ChangePassword, name="ChangePassword"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('DeleteComplaint/<int:cid>',views.DeleteComplaint,name="DeleteComplaint"),
    path('ViewBuilders/',views.ViewBuilders,name="ViewBuilders"),
    path('ViewWork/<int:id>',views.ViewWork,name="ViewWork"),
    path('ViewGallery/<int:id>',views.ViewGallery,name="ViewGallery"),
    path('Request/<int:id>',views.Request,name="Request"),
    path('MyRequest/',views.MyRequest,name="MyRequest"),
    path('Accept/<int:aid>',views.Accept,name="Accept"),
    path('Reject/<int:rid>',views.Reject,name="Reject"),
    path('ViewUpdate/<int:id>',views.ViewUpdate,name="ViewUpdate"),
    path('Feedback/',views.Feedback,name="Feedback"),

    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path('Payment/<int:rid>',views.Payment,name="Payment"),
    path('Loader/',views.Loader,name="Loader"),
    path('Payment_suc/',views.Payment_suc,name="Payment_suc"),





]