    var ps = ps2dp;
    function myFunction(){
    document.getElementById("start").disabled = true;
	$("start").addClass("btn disabled");
    var priceStart = 0;
	window.price = setInterval(function(){
	    priceStart += 1/1800;
		ps2dp = priceStart.toFixed(2);
    document.getElementById("price").textContent = "$" + ps2dp;
	},1000);
	}
function myFunction2(){
    document.getElementById("stop").disabled = true;
	$("stop").addClass("btn disabled");
	var forNum = prompt("Designated number: ");
	if ( forNum = 9633){
	    clearInterval(window.price);
	    alert("Thank you for riding with us!");
		document.getElementById("stop").disabled = true;
	    $("stop").addClass("btn disabled");
	}
	else if(forNum !== 9633){
	    var again = prompt("Invalid, try again!");
		document.getElementById("stop").disabled = false;
		$("stop").removeClass("btn disabled").addClass("btn");
	}
	}
function ins1(){
    document.getElementById("english").textContent = "INSTRUCTION IN ENGLISH!"
	}
function ins2(){
    document.getElementById("chinese").textContent = "中文说明!"
	}
function ins3(){
    document.getElementById("malay").textContent = "arahan di malay!"
	}
function ins4(){
    document.getElementById("hindi").textContent = "भारतीय में निर्देश!"
	}
