from django.http import JsonResponse
from django.shortcuts import render, redirect
from Users.models import User, StaffProfile, Subject
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index_view(request):
    return render(request, 'users/index.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        institute = request.POST.get('institute')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'status':'error', 'message':'Email address already exists.'})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status':'error', 'message':'Username already exists.'})
        
        if password != confirm_password:
            return JsonResponse({'status':'error', 'message':'Passwords does not match.'})
        
        user = User.objects.create_user(first_name=first_name.title(), last_name=last_name.title(), institute=institute.title(),
                                       email=email.lower(), username=username, password=password, role="Student")

        messages.success(request, f'{user.first_name} {user.last_name[0]} registered succesfully.')
        return JsonResponse({'status':'success','success_url':'/login/'})
    return render(request, 'users/register.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None and user.role == 'Student':
            login(request, user)
            messages.success(request, f'{user.first_name} {user.last_name[0]} logged in successfully.')
            return JsonResponse({'status':'success', 'success_url':'/'})
        else:
            return JsonResponse({'status':'error', 'message':'Invalid Username or Password.'})
    return render(request, 'users/login.html')

def staff_login_view(request,role):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None and user.role != 'Student':
            login(request, user)
            messages.success(request, f'{user.first_name} {user.last_name[0]} logged in successfully.')
            if user.role == 'Admin':
                url = '/admin/'
            elif user.role == 'HOD':
                url = '/hod/'
            else:
                url = '/teacher/'
            return JsonResponse({'status':'success', 'success_url':url})
        else:
            return JsonResponse({'status':'error', 'message':'Invalid Username or Password.'})
    return render(request, 'users/staff_login.html', context={'role':role})

def admin_index_view(request):
    return render(request, 'users/admin/admin_index.html')

def add_hod_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        department = request.POST.get('department')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'status':'error', 'message':'Email address already exists.'})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status':'error', 'message':'Username already exists.'})
        
        if StaffProfile.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'status':'error', 'message':'Phone Number already exists.'})
        
        if password != confirm_password:
            return JsonResponse({'status':'error', 'message':'Passwords does not match.'})

        user = User.objects.create_user(first_name=first_name.title(), last_name=last_name.title(),
                                       email=email.lower(), username=username, password=password, role="HOD")
        StaffProfile.objects.create(user=user, phone_number=phone_number, department=department)
        messages.success(request, f'{user.first_name} {user.last_name[0]} added succesfully.')
        return JsonResponse({'status':'success','success_url':f'/admin/update/hod/{user.id}/'})
    
    return render(request, 'users/admin/add_hod.html')

def update_hod_view(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        department = request.POST.get('department')

        if User.objects.filter(email=email).exists():
            if email != user.email:
                return JsonResponse({'status':'error', 'message':'Email address already exists.'})
        
        if User.objects.filter(username=username).exists():
            if username != user.username:
                return JsonResponse({'status':'error', 'message':'Username already exists.'})
        
        if StaffProfile.objects.filter(phone_number=phone_number).exists():
            if phone_number != user.profile.phone_number:
                return JsonResponse({'status':'error', 'message':'Phone Number already exists.'})
        
        profile = StaffProfile.objects.get(user=user)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.email = email.lower()
        user.username = username
        profile.phone_number = phone_number
        profile.department = department
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} {user.last_name[0]} profile saved successfully.')
        return JsonResponse({'status':'success', 'success_url':'/admin/'})
    return render(request, 'users/admin/update_hod.html', context={'user':user})

def admin_list_user_view(request,role):
    users = User.objects.filter(role=role).all()
    return render(request, 'users/admin/list_user.html',context={'role':role,'users':users})

def hod_index_view(request):
    return render(request, 'users/hod/hod_index.html')

def add_subject_view(request):
    if request.method == 'POST':
        subject = request.POST.get('name')
        if Subject.objects.filter(name=subject).exists():
            return JsonResponse({'status':'error', 'message':'Subject already exists.'})
        else:
            subject = Subject.objects.create(name=subject.title())
            messages.success(request, f'Subject {subject.name} added successfully.')
            return JsonResponse({'status':'success', 'success_url':'/hod/'})
    return render(request, 'users/hod/add_subject.html')

def add_teacher_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        subjects = request.POST.getlist('subjects')
        department = request.POST.get('department')



        if User.objects.filter(email=email).exists():
            return JsonResponse({'status':'error', 'message':'Email address already exists.'})
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status':'error', 'message':'Username already exists.'})
        
        if StaffProfile.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'status':'error', 'message':'Phone Number already exists.'})
        
        if password != confirm_password:
            return JsonResponse({'status':'error', 'message':'Passwords does not match.'})

        user = User.objects.create_user(first_name=first_name.title(), last_name=last_name.title(),
                                       email=email.lower(), username=username, password=password, role="Teacher")
        profile = StaffProfile.objects.create(user=user, phone_number=phone_number, department=department)
        for sub in subjects:
            subject = Subject.objects.filter(name=sub).first()
            profile.subjects.add(subject)
        profile.save()
        messages.success(request, f'{user.first_name} {user.last_name[0]} added succesfully.')
        return JsonResponse({'status':'success','success_url':f'/hod/update/teacher/{user.id}/'})
    subjects = Subject.objects.all()
    return render(request, 'users/hod/add_teacher.html',context={"subjects":subjects})

def update_teacher_view(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        username = request.POST.get('username')
        department = request.POST.get('department')
        subjects = request.POST.getlist('subjects')

        if User.objects.filter(email=email).exists():
            if email != user.email:
                return JsonResponse({'status':'error', 'message':'Email address already exists.'})
        
        if User.objects.filter(username=username).exists():
            if username != user.username:
                return JsonResponse({'status':'error', 'message':'Username already exists.'})
        
        if StaffProfile.objects.filter(phone_number=phone_number).exists():
            if phone_number != user.profile.phone_number:
                return JsonResponse({'status':'error', 'message':'Phone Number already exists.'})
        
        profile = StaffProfile.objects.get(user=user)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.email = email.lower()
        user.username = username
        profile.phone_number = phone_number
        profile.department = department
        user.save()
        for sub in subjects:
            subject = Subject.objects.filter(name=sub).first()
            profile.subjects.add(subject)
        profile.save()
        messages.success(request, f'{user.first_name} {user.last_name[0]} profile saved successfully.')
        return JsonResponse({'status':'success', 'success_url':'/hod/'})
    subjects = Subject.objects.all()
    user = User.objects.get(id=id)
    profile = StaffProfile.objects.get(user=user)
    selected_subjects = profile.subjects.values_list('name', flat=True)
    print('selected_subjects',selected_subjects)
    return render(request, 'users/hod/update_teacher.html', context={'user':user,'all_subjects':subjects,'selected_subjects':selected_subjects})

def hod_list_user_view(request,role):
    users = User.objects.filter(role=role).all()
    return render(request, 'users/hod/list_user.html',context={'role':role,'users':users})

def teacher_index_view(request):
    return render(request, 'users/teacher/teacher_index.html')

def teacher_list_user_view(request,role):
    users = User.objects.filter(role=role).all()
    return render(request, 'users/teacher/list_user.html',context={'role':role,'users':users})

def logout_view(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} logged out successfully.')
    return redirect('index-view')

def delete_user_view(request, id):
    user = User.objects.get(id=id)
    user_name = f'{user.first_name} {user.last_name[0]}'
    user.delete()
    messages.success(request, f'{user_name} deleted successfully.')
    return redirect(request.META.get('HTTP_REFERER', '/'))