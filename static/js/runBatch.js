/**
 * Created by pridemai on 10/22/15.
 */
/**
 * Created by smileya on 10/22/2015.
 */

/**
Let's see if i can remember how this shit is supposed to work
 */
function runBatch(){
    $.ajax({
        url : "/ajax_handler/run_batch/",
        type: "post",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'master_files' : $('input[name="master_files"]:checked').map(function(){
      return $(this).val();
    }).get(),
            'source_files' : $('input[name="source_files"]:checked').map(function(){
      return $(this).val();
    }).get()
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

