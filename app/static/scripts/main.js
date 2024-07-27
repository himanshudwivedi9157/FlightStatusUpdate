// document.addEventListener('DOMContentLoaded', function() {
//     console.log('JavaScript Loaded');

//     const button = document.getElementById('check-status');
//     const container = document.getElementById('flight-status-container');

//     if (button) {
//         button.addEventListener('click', async function() {
//             try {
//                 const response = await fetch('/flights');
//                 const data = await response.json();
//                 console.log(data);
//                 container.innerHTML = ''; // Clear any previous content
//                 data.forEach(flight => {
//                     const flightElement = document.createElement('div');
//                     flightElement.classList.add('flight');
//                     flightElement.innerHTML = `
//                         <p>Flight Number: ${flight.flight_number}</p>
//                         <p>Status: ${flight.status}</p>
//                         <p>Gate: ${flight.gate}</p>
//                     `;
//                     container.appendChild(flightElement);
//                 });
//             } catch (error) {
//                 console.error('Error:', error);
//             }
//         });
//     }
// });



document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript Loaded');

    const button = document.getElementById('check-status');
    const tbody = document.getElementById('flight-status-body');

    if (button) {
        button.addEventListener('click', async function() {
            try {
                const response = await fetch('/flights');
                const data = await response.json();
                console.log(data);
                tbody.innerHTML = ''; // Clear any previous content

                data.forEach(flight => {
                    const row = document.createElement('tr');
                    row.classList.add(getStatusClass(flight.status));
                    row.innerHTML = `
                        <td>${flight.flight_number}</td>
                        <td>${flight.status}</td>
                        <td>${flight.gate}</td>
                    `;
                    tbody.appendChild(row);
                });
            } catch (error) {
                console.error('Error:', error);
            }
        });
    }

    function getStatusClass(status) {
        switch (status.toLowerCase()) {
            case 'on time':
                return 'on-time';
            case 'delayed':
                return 'delayed';
            case 'cancelled':
                return 'cancelled';
            default:
                return '';
        }
    }
});

