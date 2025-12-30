from django.urls import path
from Builder import views
app_name="Builder"

urlpatterns=[
    path('HomePage/',views.HomePage, name="HomePage"),
    path('MyProfile/',views.MyProfile, name="MyProfile"),
    path('EditProfile/',views.EditProfile, name="EditProfile"),
    path('ChangePassword/',views.ChangePassword, name="ChangePassword"),
    path('WorkerRegistration/',views.WorkerRegistration,name="WorkerRegistration"),


    path('Work/',views.Work,name="Work"),
    path('DeleteWork/<int:did>',views.DeleteWork,name="DeleteWork"),
    path('Gallery<int:id>',views.Gallery,name="Gallery"),
    path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
    path('Accept/<int:aid>',views.Accept,name="Accept"),
    path('Reject/<int:rid>',views.Reject,name="Reject"),
    path('ViewWorkers/<int:rid>',views.ViewWorkers,name="ViewWorkers"),
    path('assign/<int:wid>/<int:rid>',views.assign,name="assign"),
    path('Amount/<int:aid>',views.Amount,name="Amount"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('Logout/',views.Logout,name="Logout"),


]