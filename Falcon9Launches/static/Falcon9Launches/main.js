$(document).ready(function(){

    configDeleteButton()
  
});



function configDeleteButton(){

let csrf = $('input[name="csrfmiddlewaretoken"]')[0].value
$('.buttonDelete').each(function(index) {
    console.log( $( this ).html() ) 
    let id = $(this).data('id')
    $( this ).click( function(){
        // alert(`clicked button with id ${id}`)
        // $.post( '', { id: id, csrf: 1234 } );
        $.ajax({
            url: `boosters/delete/${id}`,
            type: 'DELETE',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", csrf);
            },
            // data: {csrfmiddlewaretoken: csrf},
             success: function (result) {
                // console.log(`received result:${JSON.stringify(result)}`);
                if (result.success === 'true'){
                    location.reload() 
                }
            }
        });
    })
})
}