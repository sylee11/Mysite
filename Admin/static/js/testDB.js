function test(){
	alert("Hello");
	// $(document).ready(function() {
	$("#dataTable2").dataTable().fnDestroy();
    $('#dataTable2').DataTable( {
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/test/",
            "type": "POST"
        },
        Destroy: true,
        retrieve: true,
        start : '1',
        // "columns": [
        //     { "data": "first_name" },
        //     { "data": "last_name" },
        //     { "data": "position" },
        //     { "data": "office" },
        //     { "data": "start_date" },
        //     { "data": "salary" }
        // ]
    } );
	// } );
}
$(document).ready(function(){
    $('#dataTable2').DataTable()

})