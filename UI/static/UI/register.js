$(document).ready(function() {
    $('#register-form').submit(function(event) {
        event.preventDefault();

        var userData = {
            username: $('#username').val(),
            email: $('#email').val(),
            password: $('#password').val()
        };

        $.ajax({
            url: '/api/register/',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(userData),
            success: function(data) {
                alert('Registration successful! Please log in.');
                window.location.href = '/login/';
            },
            error: function() {
                alert('Registration failed');
            }
        });
    });
});