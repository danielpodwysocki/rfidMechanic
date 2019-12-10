//A script that pulls a json file and then adds divs containg information about players' hands
var cards=[];
playerSlider = document.getElementById("playerSlider");
var playerCount=4;

function toNames(card){
	//returns a string with a human-friendly represantation of the card
	suits = ['&#9827;','&#9829;','&#9824;','&#9830;']; //unicode for clubs, hearts, spades and diamonds (CHaSeD order)
	values = ['1','2','3','4','5','6','7','8','9','10','J','Q','K'];
	
	//card numbers go in CHSD order, so 1 to 13 are ace to king of clubs, 14 is the ace of hearts and so on 
	suit = Math.ceil(card/13)-1; //-1 for the arr indexes and for the suit*13 to work
	value = card - suit*13 -1;
	
	return values[value]+suits[suit];
}

function updateHoldEm(){
	//a function that updates the cards for texas hold em (both player hands and the board, the reason we scan the board even though it's known
	// is because we might want to calculate the winning chances for each player)
	
	var board = [];
	if(cards.length>3){ 
		let playerCount = Math.ceil(cards.length/2);
		
		let cont = document.getElementById("holdEmGrid");
		
		cont.innerHTML="";
		
		for(i=0;i<playerCount;i++){
			cont.innerHTML+="<div class='holdEmPlayer'>&#13<div class='holdEmProb'></div></div>&#13;"; //&#13 is CR
		}
		let players = document.getElementsByClassName("holdEmPlayer");
		
		let player = 0;
		
		for(i=0;i<cards.length;i++){// we "deal" the cards into the divs
			
			if(player==playerCount) player = 0; //if we already dealt a card for each player, we want to go around one more time
			players[player].innerHTML+=toNames(cards[i]);
			player++;
			
		}
	}
}

function updateCards(playerCount){
	//updates the amount of player divs and puts the translated card names inside of them
	cont = document.getElementById("equalDealGrid");
	cont.innerHTML="";
	for(i=0;i<playerCount;i++){
		cont.innerHTML+="<div class='player'> </div>&#13;";
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
	fetch("http://192.168.0.1:8080/get_cards")
		.then(resp=>resp.json())
		.then(resp => {
			cards=resp;
			updateCards(playerCount);
			updateHoldEm();
		});
}


playerSlider.oninput = function() {
	playerCount = this.value;
	var playerCounter = document.getElementById('playerCounter');
	playerCounter.innerHTML = playerCount;
	updateCards(playerCount);
}

clearCardsBtn = document.getElementById('clearCardsBtn');
clearCardsBtn.onclick = function(){
	var xhr = new XMLHttpRequest();
	var url = "clear_cards";
	xhr.open("POST",url,true);
	
	xhr.send();
	
}

getCards();

setInterval(getCards,1000)