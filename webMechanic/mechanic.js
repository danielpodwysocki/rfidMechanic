//A script that pulls a json file and then adds divs containg information about players' hands
var cards=[];
playerSlider = document.getElementById("playerSlider");
var playerCount=4;
function updateCards(playerCount){
	cont = document.getElementById("equalDealGrid");
	cont.innerHTML="";
	for(i=0;i<playerCount;i++){
		cont.innerHTML+="<div class='player'> </div>";
	}
	players = document.getElementsByClassName("player");
	p = 0;
	for(c=0;c<cards.length;c++){
		if(p>=playerCount) p=0;
		players[p].innerHTML+=cards[c]+" ";
		p++;
	}
}

updateCards(playerCount);

function getCards(){
	//the ip can be hardcoded, because the app is hosted on the rapsberry pi access point
	//right now it's localhost for testing purposes
	fetch("http://127.0.0.1:8080/getcards")
		.then(resp=>resp.json())
		.then(resp => {
			cards=resp;
			updateCards(playerCount);
		});
}


playerSlider.oninput = function() {
	playerCount = this.value;
	updateCards(playerCount);
}
getCards();
console.log(cards)

setInterval(getCards,1000)