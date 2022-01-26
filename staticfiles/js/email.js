function validate(){
    var number = document.getElementById("id_email").value;

    var regx = /@vitbhopal.ac.in/;

    if(regx.test(number)){

        var r = document.getElementById("check");
        r.innerHTML = "Valid";
        r.style.color = "green";

    }
    else{

        var r = document.getElementById("check").addEventListener("click", function(event){
            event.preventDefault()
          });
          
        r.innerHTML = "wwwrrrooonnnggg";
        r.style.color = "red";
        
    }

}