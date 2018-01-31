function staff(){
    var check = prompt("Password: ");
	if (check == "staff"){
	    $("getNum").removeClass("btn btn-success disabled").addClass("btn btn-success")
		document.getElementById("getNum").disabled = false;
		}
		}
function getNum(){
    window.num = Math.floor(Math.random() * (9999 - 1000 + 1)) + 1000;
    document.getElementById("random").textContent = num;
	document.getElementById("getNum").disabled = true;
	$("getNum").addClass("btn disabled")
	}
