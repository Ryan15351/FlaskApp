function register(){

    let form = document.getElementById("register-form") 
    let email = document.getElementById("email");
    let password = document.getElementById("senha");
    let numero = document.getElementById("numero")
    let nome = document.getElementById("nome")
    let credentials = "email= " + email.value + "&password= " + password.value + "&numero= " + numero.value +"&nome= "+ nome.value;
    console.log(credentials)
    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function(){
        if (xml.status == 200){
            console.log(xml.response);
        }
    };
    xml.open("POST", "/register");
    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xml.send(credentials);



};
