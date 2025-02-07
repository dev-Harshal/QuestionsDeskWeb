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

const staffLoginForm = document.getElementById('staffLoginForm')
if (staffLoginForm) {
    staffLoginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(staffLoginForm)
        const role = document.getElementById('role').value
        url = `/staff/login/${role}/`
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

const addHodForm = document.getElementById('addHodForm')
if (addHodForm) {
    addHodForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addHodForm)
        fetch('/admin/add/hod/', {
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

const addTeacherForm = document.getElementById('addTeacherForm')
if (addTeacherForm) {
    addTeacherForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addTeacherForm)
        fetch('/hod/add/teacher/', {
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
            }
            else {
                popAlert(data)
            }
        })
    })
}

const addSubjectForm = document.getElementById('addSubjectForm')
if (addSubjectForm) {
    addSubjectForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(addSubjectForm)
        fetch('/hod/add/subject/', {
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