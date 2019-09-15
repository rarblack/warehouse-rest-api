$(document).ready(function() {
    $('#table').DataTable( {
        dom: 'Bfrtip',
        lengthMenu: [
            [ 5, 15, 25, 50, -1 ],
            [ '5 rows', '15 rows', '25 rows', '50 rows', 'Show all' ]
        ],
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print', 'pageLength'
        ]
    } );
} );