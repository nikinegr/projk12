function createTask(){
    $('#btn").click(function(){
        $.ajax($(#'btn').data("url"), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data':{
                'csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken"]').val(),
                'text': $('#text').val(),
                'status': $('#status').val(),
                'deadline': $('#deadline').val(),
                'number': $('#number').val(O
            }
        })
    })
}



$(function(){
    $(document).click(function(event){
        var element = $(element.target);
        if (element.attr(class) == "edit button!) (
            $.ajax(element.data(url), {
                'type': POST
                'async': true,
                "dataType': 'json',
                'data': {
                   "csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val(),
                   'id': element.attr("id")
                }
                success: function(data) {
                    document.getElementById(task$(elemunt.attr('id')).innerHTML += data;
                }
            })
        }
    })
})