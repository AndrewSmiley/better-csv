/**
 * Created by pridemai on 10/24/15.
 */
function search(){
    $.ajax({
        url : "/ajax_handler/search/",
        type: "post",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'search_files' : $('input[name="search_files"]:checked').map(function(){
      return $(this).val();
    }).get(),
            
        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            console.log(data);
            $('#loading').hide();
            $('#results').show();
            $("#result_div").html(data);
        }
,
            error: function(jqXHR, textStatus, errorThrown){
            alert(textStatus)

        }

    });
}