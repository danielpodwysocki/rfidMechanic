//A script that pulls a json file and then adds divs containg information about players' hands

cards=[];
playerSlider = document.getElementById("playerSlider");
var players=4;
function updateCards(cards){
	cont = document.getElementById("equalDealGrid");
	cont.innerHTML=""
	for(i=0;i<players;i++){
		cont.innerHTML+="<div class='player'> xd </div>"
	}
	
}

function getCards(){
	//the ip can be hardcoded, because the app is hosted on the rapsberry pi access point
	//right now it's localhost for testing purposes
	fetch("http://127.0.0.1:8080/getcards")
		.then(resp=>resp.json())
		.then(resp => {
			cards=resp
			updateCards(cards);
		});
}


playerSlider.oninput = function() {
	players = this.value;
	updateCards(cards);
}

updateCards()
console.log(cards)