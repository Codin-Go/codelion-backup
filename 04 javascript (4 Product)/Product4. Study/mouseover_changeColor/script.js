function change(v) {
	var target = document.getElementById("target");
	if (v == "imgA") {
		target.className = "a";
		target2.document = "aa" ; 
	} else if (v == "imgB") {
		target.className = "b";
	} else if (v == "imgC") {
		target.className = "c";
	} else if (v == "imgD") {
		target.className = "d";
	} else if (v == "imgE") {
		target.className = "e";
	} else {
		target.className = "";
	}
}
function changeReset() {
	var target = document.getElementById("target");
	target.className = "";

	var target2 = document.getElementById("target2");
	target2.className = "";

}