$(document).ready(function() {
    $('#table').DataTable( {
        "scrollX": true,
        dom: 'Bfrtip',
        lengthMenu: [
            [ 10, 25, 35, 50, -1 ],
            [ '10 rows', '25 rows', '35 rows', '50 rows', 'Show all' ]
        ],
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print', 'pageLength'
        ]
    } );
} );