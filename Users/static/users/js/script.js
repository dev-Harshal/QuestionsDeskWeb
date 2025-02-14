function popAlert(data) {
    let status
    let alertContainer = document.getElementById('alertContainer');
    let alert = document.createElement('div');
    alertContainer.innerHTML = ''
    alert.id = 'alert'
    
    if (data.status === 'error') {
        status = 'danger'
    }
    else{
        status = data.status
    }
    alert.className = `alert alert-${status}`
    alert.role = 'alert'
    alert.innerHTML = `${data.message}`
    setTimeout(() => {
        alertContainer.appendChild(alert)
        setTimeout(() => {
            alert.style.display = 'none'
        },5000)
    },200)
}

alertBox = document.getElementById('alert')
if (alertBox) {
    setTimeout(function() {
        alertBox.style.display = 'none';
    }, 5000);
}

// -- USERS FORMS --

const registerForm = document.getElementById('registerForm')
if (registerForm) {
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(registerForm)
        fetch('/register/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data);
            }
        })

    })
}

const loginForm = document.getElementById('loginForm')
if (loginForm) {
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(loginForm)

        fetch('/login/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

// -- STAFF FORMS --

const staffLoginForm = document.getElementById('staffLoginForm')
if (staffLoginForm) {
    staffLoginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(staffLoginForm)
        const role = document.getElementById('role').value
        url = `/${role}/login/`
        fetch(url, {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

const staffProfileForm = document.getElementById('staffProfileForm')
if (staffProfileForm) {
    staffProfileForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(staffProfileForm)
        const role = document.getElementById('role').value
        url = `/${role}/profile/`
        fetch(url, {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                popAlert(data)
            }
            else {
                popAlert(data)
            }
        })
    })
}

const changePasswordForm = document.getElementById('changePasswordForm')
if (changePasswordForm) {
    changePasswordForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(changePasswordForm)
        fetch('/change-password/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                popAlert(data)
            }
            else {
                popAlert(data)
            }
        })
    })
}

// -- ADMIN FORMS --

const addHodForm = document.getElementById('addHodForm')
if (addHodForm) {
    addHodForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addHodForm)
        fetch('/admin/create/hod/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

const updateHodForm = document.getElementById('updateHodForm')
if (updateHodForm) {
    updateHodForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(updateHodForm)
        const id = document.getElementById('id').value
        url = `/admin/update/hod/${id}/`
        
        fetch(url, {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

// -- HOD FORMS --

const addSubjectForm = document.getElementById('addSubjectForm')
if (addSubjectForm) {
    addSubjectForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addSubjectForm)
        fetch('/hod/create/subject/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

const updateSubjectForm = document.getElementById('updateSubjectForm')
if (updateSubjectForm) {
    updateSubjectForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(updateSubjectForm)
        const id = document.getElementById('id').value
        url = `/hod/update/subject/${id}/`
        
        fetch(url, {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
        .catch(error => {
            console.error(error)
        })
    })
}

const addTeacherForm = document.getElementById('addTeacherForm')
if (addTeacherForm) {
    addTeacherForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addTeacherForm)
        fetch('/hod/create/teacher/', {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
            }
            else {
                popAlert(data)
            }
        })
    })
}

const updateTeacherForm = document.getElementById('updateTeacherForm')
if (updateTeacherForm) {
    updateTeacherForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(updateTeacherForm)
        const id = document.getElementById('id').value
        url = `/hod/update/teacher/${id}/`
        
        fetch(url, {
            method : 'POST',
            headers : {
                'X-CSRFToken':document.querySelector('input[name="csrfmiddlewaretoken"]').value
            },
            body : formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                window.location.href = data.success_url
                popAlert(data)
            }
            else {
                popAlert(data)
            }
        })
    })
}

