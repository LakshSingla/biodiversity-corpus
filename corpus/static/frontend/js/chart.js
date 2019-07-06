let ctx;
ctx = document.getElementById('sentiment-chart').getContext('2d');
const sentimentChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [{
            label: 'Sentiments',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [3, 10, 5]
        }]
    },
    options: {
        responsive: true,
        elements: {
            rectangle: {
                borderWidth: 2,
            },
        },
        scales: {
            yAxes: [{
                barThickness: 10,
            }]
        }

    }

});

ctx = document.getElementById('timeseries-chart').getContext('2d');
const timeseries = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            'Jan',
            'Feb',
            'March',
            'April',
            'May',
            'June',
            'July',
            'Aug',
            'Sept',
            'Oct',
            'Nov',
            'Dec',
        ],
        datasets: [{
            label: 'Sentiments',
            borderColor: 'rgb(255, 99, 132)',
            fill: false,
            data: [2, 3, 5, 5, 5, 6, 5, 3, 5, 3, 1, 2]
        }]
    },

});

ctx = document.getElementById('statewise-chart').getContext('2d');
const statewise = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: [
            'State 1',
            'State 2',
            'State 3',
            'Other',
        ],
        datasets: [{
            label: 'Sentiments',
            backgroundColor: 'rgb(99, 231, 12)',
            borderColor: 'rgb(255, 99, 132)',
            fill: false,
            data: [2, 10, 5, 5]
        }]
    },

});