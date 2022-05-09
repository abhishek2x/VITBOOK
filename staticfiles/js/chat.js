
        
    $('#send').click(function (e) { 
        e.preventDefault();
        $('#container').scrollTop($("#container").prop("scrollHeight"));
    });


    $('#textbox').keypress(function (e) { 
        if(e.which == 13){
            $('#send').click();
            e.preventDefault();
        }
    });
