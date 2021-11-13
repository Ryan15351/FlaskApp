function userLogin(){

    let form = document.getElementById("login-form") 
    let email = document.getElementById("email");
    let password = document.getElementById("senha");
    let credentials = "email= " + email.value + "&password= " + password.value;
    console.log(credentials)
    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function(){
        if (xml.status == 200){
            console.log(xml.response);
        }
    };
    xml.open("POST", "/login");
    xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xml.send(credentials);



};


function back() {
    window.history.back('/home')
};