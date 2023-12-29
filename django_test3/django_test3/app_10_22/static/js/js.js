function test(){
$('#btn').click(function(){
    let form data new FormData()
    form data.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]").val())
    form_data.append(name, $('name').val())
    form_data.append("file", document.getElementById('file').files[0])
    $.ajax('/test/',{
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data':{
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        'email': $('#email').val(),
        'name': $('#nome').val(),
        'password': $('#password').val()
        'test': $('#inp').val()
        },
        'success': function(data) {
        document.getElementById("glw").innerHTML = data
        }
    })
})}

$(document).ready(function(){
    test();
})








