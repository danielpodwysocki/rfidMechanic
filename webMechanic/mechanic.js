//A script that pulls a json file and then adds divs containg information about players' hands
var cards=[];
playerSlider = document.getElementById("playerSlider");
var playerCount=4;

function toNames(card){
	//returns a string with a human-friendly represantation of the card
	suits = ['C','H','S','D'];
	values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K'];
	
	//card numbers go in CHSD order, so 1 to 13 are ace to king of clubs, 14 is the ace of hearts and so on 
	suit = Math.ceil(card/13)-1; //-1 for the arr indexes and for the suit*13 to work
	value = card - suit*13 -1;
	
	return suits[suit]+values[value];
}

function updateCards(playerCount){
	//updates the amount of player divs and puts the translated card names inside of them
	cont = document.getElementById("equalDealGrid");
	cont.innerHTML="";
	for(i=0;i<playerCount;i++){
		cont.innerHTML+="<div class='player'> </div>";
	}
	players = document.getElementsByClassName("player");
	p = 0;
	for(c=0;c<cards.length;c++){
		if(p>=playerCount) p=0;
		players[p].innerHTML+=toNames(cards[c])+" ";
		p++;
	}
}

updateCards(playerCount);

function getCards(){
	//the ip can be hardcoded, because the app is hosted on the rasp pi access point dedicated just to running that app
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