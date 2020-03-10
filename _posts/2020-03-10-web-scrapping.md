---
title: "Web Scrapping"
date: 2020-02-26
categories: Tugas
---

<!--
<html>
<script src="http://code.jquery.com/jquery-3.3.1.js"></script>

<script>
     $(document).ready(function(){
        $.getJSON('headline.json',function(data){
            var headline_data = '';
            var i = 1;
            headline_data += "<table border='1'><tr><td>No</td><td>Kategori</td><td>Judul Artikel</td><td>Waktu</td></tr>"
            $.each(data, function(key, value) {
                headline_data += '<tr>';
                headline_data += '<td>'+i+'</td>'
                headline_data += '<td>'+value.kateg+'</td>'
                headline_data += '<td>'+value.judul+'</td>'
                headline_data += '<td>'+value.waktu+'</td>'
                headline_data += '</tr>';
                i = i + 1;
            });
            $('#headline').append(headline_data);
        });
    });
</script>

<body>
    <h1>Head Line Republika Online</h1>
    <div id="headline"></div>
</body>
</html>
-->

<body>
	<link rel="shortcut icon" href="https://python-scripts.com/wp-content/uploads/2019/10/beautifulsoup-html-parsing-example.png">
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.20/js/dataTables.bootstrap4.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.css" rel="stylesheet">
    <link href="https://cdn.datatables.net/1.10.20/css/dataTables.bootstrap4.min.css" rel="stylesheet">
    <div class="row">
        <div class="col-md-10 offset-md-1">
            <hr>
            <h1 class="d-flex justify-content-center">Tugas Scrapping - Proyek 1</h1>
            <hr>
        </div>
    </div>
    <div class="row">
        <div class="col-md-10 offset-md-1">
            <table id="bimz" class="table table-striped table-bordered">
                <thead>
                    <tr>
                        <th>Judul</th>
                        <th>Kategori</th>
                        <th>Time</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
<script type="text/javascript">
    $(document).ready(function () {
        $('#bimz').DataTable({
            processing: true,
            "ajax": {
                "url": "headline.json",
                dataSrc:""
            },
            "columns": [
                { "data": "judul" },
                { "data": "kateg" },
                { "data": "waktu" }
            ]
        });
    });
</script>