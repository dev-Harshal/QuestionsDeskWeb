from django.urls import path
from Users.views import *

urlpatterns = [
    path('', index_view, name='index-view'),
    path('register/', register_view, name='register-view'),
    path('login/', login_view, name='login-view'),

    path('staff/login/<str:role>/', staff_login_view, name='staff-login-view'),

    path('admin/', admin_index_view, name='admin-index-view'),
    path('admin/add/hod/', add_hod_view, name='add-hod-view'),
    path('admin/update/hod/<int:id>/', update_hod_view, name='update-hod-view'),
    path('admin/list/<str:role>/', admin_list_user_view, name='admin-list-user-view'),

    path('hod/', hod_index_view, name='hod-index-view'),
    path('hod/add/subject/', add_subject_view, name='add-subject-view'),
    path('hod/add/teacher/', add_teacher_view, name='add-teacher-view'),
    path('hod/update/teacher/<int:id>/', update_teacher_view, name='update-teacher-view'),
    path('hod/list/<str:role>/', hod_list_user_view, name='hod-list-user-view'),

    path('teacher/', teacher_index_view, name='teacher-index-view'),
    path('teacher/list/<str:role>/', teacher_list_user_view, name='teacher-list-user-view'),

    path('logout/', logout_view, name='logout-view'),
    path('delete/<int:id>', delete_user_view, name='delete-user-view')
]
