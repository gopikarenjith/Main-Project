from django.urls import path
from Worker import views
app_name="Worker"
urlpatterns = [
    path('HomePage/',views.HomePage, name="HomePage"),
    path('MyProfile/',views.MyProfile, name="MyProfile"),
    path('ChangePassword/',views.ChangePassword, name="ChangePassword"), 
    path('EditProfile/',views.EditProfile, name="EditProfile"),
    path('ViewAssign/',views.ViewAssign,name="ViewAssign"),
    path('UpdateAssign/<int:id>/<int:status>',views.UpdateAssign,name="UpdateAssign"),
    path('Updates/<int:id>',views.Updates,name="Updates"),
    path('Feedback/',views.Feedback,name="Feedback"),
    path('Logout/',views.Logout,name="Logout"),


    ]

