
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
           });
});
$('#suggestion').keyup(function(){
        var query;
        query = $(this).val();
        $.get('/rango/suggest_category/', {suggestion: query}, function(data){
                $('#cats').html(data);
            });
});
$('button.rango-add').click(function(){
        var catid;
        var title;
        var url;
        catid = $(this).attr("data-catid");
        title = $(this).attr("data-title");
        url = $(this).attr("data-url");
        $.get('/rango/auto_add_page/', {data_catid: catid, data_title: title, data_url: url}, function(data){
                $(this).hide();
                $('#pages').html(data);
            });
});