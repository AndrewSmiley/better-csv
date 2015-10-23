/**
 * Created by smileya on 10/22/2015.
 */

/**
Let's see if i can remember how this shit is supposed to work
 */
function getFilesInFolder(){
    $.ajax({
        url : "/ajax_handler/get_files/",
        type: "get",
        data : {
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
            'folder' : $('.folder').find(":selected").text()

        },
        dataType: "html",
        success: function(data, textStatus, jqXHR){
            //try to append the html data recieved
            console.log(data)
            $("#filename").html(data);
          //
          //  $("#scholarship_dialog").dialog({
          //      width: '600px',
          //      padding: '100px',
          //      //#height: '500px',
          //      autoOpen: false,
          //      show: {
          //          effect: "blind",
          //          duration: 1000
          //      },
          //      hide: {
          //          effect: "explode",
          //          duration: 1000
          //      }
          //  });
          //
          //  $("#registration_id").attr('value', registration_id)
          //$("#scholarship_dialog").dialog("open");


        }
,
            error: function(jqXHR, textStatus, errorThrown){
            alert("Unable to fetch scholarship form. Please try again or contact the site administrators.")

        }

    });
}

