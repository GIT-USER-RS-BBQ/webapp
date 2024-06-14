$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();

        var credentials = {
            username: $('#username').val(),
            password: $('#password').val()
        };

        $.ajax({
            url: '/api/token/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(credentials),
            success: function(data) {
                localStorage.setItem('token', data.access);
                window.location.href = '/';
            },
            error: function() {
                alert('Login failed');
            }
        });
    });
});