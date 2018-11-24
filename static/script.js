function sendData(){
    var loader = document.createElement('div');
    loader.setAttribute("class", "loader");
    document.getElementById("content").appendChild(loader);
    document.getElementById("main-content").setAttribute("hidden", "true");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText != "error"){
                var form = document.createElement('form');
                form.setAttribute("action", "/image");
                form.setAttribute("method", "POST");
                var imageData  = document.createElement('input');
                imageData.setAttribute("type", "text");
                imageData.setAttribute("name", "image-data");
                imageData.setAttribute("id", "image-data");
                imageData.setAttribute("value", "data:image/jpg;base64, "+this.responseText);

                document.body.appendChild(form);
                form.appendChild(imageData);
                form.submit();
            }
        
        }
    };
    xhttp.open("POST", "http://127.0.0.1:5000/api/create", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    sendString = '{\n   '
    sendString += '"first_name": "';
    sendString += document.getElementById("first_name").value + "$$";
    sendString += '",\n    "last_name": "';
    sendString += document.getElementById("last_name").value + "$$";
    sendString += '",\n    "email": "';
    sendString += document.getElementById("email").value + "$$";
    sendString += '",\n    "dob": "';
    sendString += document.getElementById("date_of_birth").value + "$$";
    
    //console.log(sendString);
    
    var file = document.getElementById('image').files[0];
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function () {
        var b64long = reader.result;
        var b64 = b64long.substring(b64long.indexOf(",")+1,b64long.length);
        //console.log(b64);
        sendString += '",\n    "image-data": "';
        sendString += b64;
        sendString += '"\n}';
        xhttp.send(sendString);
      };
};


 
