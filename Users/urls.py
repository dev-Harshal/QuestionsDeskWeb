from django.urls import path
from Users.views import *

urlpatterns = [
    # Users
    path('', index_view, name='index-view'),
    path('register/', register_view, name='register-view'),
    path('login/', login_view, name='login-view'),
    path('logout/', logout_view, name='logout-view'),

    # Staff Common
    path('<str:role>/login/', staff_login_view, name='staff-login-view'),
    path('<str:role>/profile/', staff_profile_view, name='staff-profile-view'),
    path('change-password/', staff_change_password_view, name='staff-changepassword-view'),
    path('delete/<int:id>', staff_delete_user_view, name='staff-delete-user-view'),
    
    #Admin
    path('admin/', admin_index_view, name='admin-index-view'),
    path('admin/create/hod/', admin_create_hod_view, name='admin-create-hod-view'),
    path('admin/update/hod/<int:id>/', admin_update_hod_view, name='admin-update-hod-view'),
    path('admin/list/<str:role>/', admin_list_user_view, name='admin-list-user-view'),

    #HOD
    path('hod/', hod_index_view, name='hod-index-view'),
    path('hod/create/subject/', hod_create_subject_view, name='hod-create-subject-view'),
    path('hod/update/subject/<int:id>/', hod_update_subject_view, name='hod-update-subject-view'),
    path('hod/delete/subject/<int:id>/', hod_delete_subject_view, name='hod-delete-subject-view'),
    path('hod/list/subject/', hod_list_subject_view, name='hod-list-subject-view'),
    path('hod/create/teacher/', hod_create_teacher_view, name='hod-create-teacher-view'),
    path('hod/update/teacher/<int:id>/', hod_update_teacher_view, name='hod-update-teacher-view'),
    path('hod/list/<str:role>/', hod_list_user_view, name='hod-list-user-view'),

    path('teacher/', teacher_index_view, name='teacher-index-view'),
    path('teacher/list/<str:role>/', teacher_list_user_view, name='teacher-list-user-view'),

]
