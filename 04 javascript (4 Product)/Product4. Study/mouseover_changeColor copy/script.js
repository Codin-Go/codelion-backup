function change(v) {
	// var target = document.getElementById("target");
	var target = document.getElementById("target").innerHTML;
	if (v == "imgA") {
		// target.className = "a";
		target = "Good Day!";  
	// } else if (v == "imgB") {
	// 	target.className = "b";
	// } else if (v == "imgC") {
	// 	target.className = "c";
	// } else if (v == "imgD") {
	// 	target.className = "d";
	// } else if (v == "imgE") {
	// 	target.className = "e";
	} else {
		// target.className = "";
		target = "Good Day!";  
	}
}
function changeReset() {
	// var target = document.getElementById("target");
	// target.className = "";
	var target = document.getElementById("target").innerHTML;
	// target.className = "";
	target = "";
	""; 

}

//   document.getElementById("demo").innerHTML = "Good day!";

var day = Math.floor(timeDiff / (1000 * 60 * 60 * 24) / 365 + 1);
$('#love').text('Y+' + day);
