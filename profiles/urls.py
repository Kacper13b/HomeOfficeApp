from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path("<int:pk>/", views.ProfileDetailView.as_view(), name='detail'),
    path("<int:pk>/editprofile_page/", views.ProfileEditView.as_view(), name='edit_profile_page'),
    path("<int:pk>/editprofile/", views.ProfileEditPageView.as_view(), name='edit_profile'),
]