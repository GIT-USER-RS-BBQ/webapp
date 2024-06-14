$(document).ready(function() {
    // Function to load tipps from the server
    function loadTipps() {
        $.ajax({
            url: '/api/tipps/',
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            },
            success: function(data) {
                $('#tipp-list').empty();
                data.forEach(function(tipp) {
                    $('#tipp-list').append(
                        '<li data-id="' + tipp.id + '">' +
                        '<span class="tipp-title">' + JSON.stringify(tipp) + '</span>' +
                        '<div class="tipp-actions">' +
                        '<button class="complete-tipp">Complete</button>' +
                        '</div>' +
                        '</li>'
                    );
                });
            }
        });
    }

    function loadMatches() {
        $.ajax({
            url: '/api/matches/',
            method: 'GET',
            // headers: {
            //     'Authorization': 'Bearer ' + localStorage.getItem('token')
            // },
            success: function(data) {
                $('#match-list').empty();
                data.forEach(function(match) {
                    $('#match-list').append(
                        '<li data-id="' + match.id + '">' +
                        '<span class="match-title">' + JSON.stringify(match) + '</span>' +
                        '<img src="/static/UI/resources/flags/'+match.home_team+'.png">' +
                        '<div class="match-actions">' +
                        '<button class="complete-match">Complete</button>' +
                        '</div>' +
                        '</li>'
                    );
                });
            }
        });
    }

    // Load tipps on page load
    // loadTipps();
    loadMatches();

});