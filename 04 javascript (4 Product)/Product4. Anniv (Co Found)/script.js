function change(v) {
	var target = document.getElementById("target");
	if (v == "imgA") {
		target.className = "a";
	} else if (v == "imgB") {
		target.className = "b";
	} else if (v == "imgC") {
		target.className = "c";
	} else {
		target.className = "";
	}
}

function changeReset() {
	var target = document.getElementById("target");
	target.className = "";
}

// 
var z = 0;
  
function changeText(v) {
	var target2 = document.getElementById("target").innerHTML;
	if (v == "imgA") {
		target2 = "hi";
	} else if (v == "imgB") {
		target2 = "hey";
	} else if (v == "imgC") {
		target2 = "how";
	} else {
		target2 = "";
	}
  // document.getElementById("demo").innerHTML = "hi";
}


let text = "here we are"; 
