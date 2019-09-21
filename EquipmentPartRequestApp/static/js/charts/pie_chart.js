$(document).ready(function() {

    let requests_lengths = {
        'pending': 0,
        'accepted': 0,
        'cancelled': 0,
        'closed': 0,
    };

    function get_length(value){
        if(value.status === 0)
            requests_lengths['pending'] = requests_lengths['pending'] + 1;
        if(value.status === 1)
            requests_lengths['accepted'] = requests_lengths['accepted'] + 1;
        if(value.status === 2)
            requests_lengths['cancelled'] = requests_lengths['cancelled'] + 1;
        if(value.status === 3)
            requests_lengths['closed'] = requests_lengths['closed'] + 1;
    }

    setTimeout(function () {
        $.ajax({
            url: "http://localhost:8000/api/requests/list/requests/b5365a061939e26d935afd01cd29086c0328eb206c7547603202fc31ef005f5bcd76a53862316a3d28085a052e3395d43fb62e0d5893c430a3b4af14590cd168",
            contentType: "application/json",
            dataType: "json",
            success: function (data) {
                data.forEach(get_length);

                //pie
                var ctxP = document.getElementById("pieChart").getContext('2d');
                var myPieChart = new Chart(ctxP, {
                    type: 'pie',
                    data: {
                        labels: ["Pending", "Accepted", "Cancelled", "Closed"],
                        datasets: [
                            {
                                data: [
                                    requests_lengths['pending'],
                                    requests_lengths['accepted'],
                                    requests_lengths['cancelled'],
                                    requests_lengths['closed']
                                ],
                                backgroundColor: ["#FDB45C", "#46BFBD", "#F7464A", "#949FB1"],
                                hoverBackgroundColor: ["#FFC870", "#5AD3D1", "#FF5A5E", "#A8B3C5"]
                            }
                        ]
                    },
                    options: {
                        responsive: true
                    }
                });

            }});
    },1);
});