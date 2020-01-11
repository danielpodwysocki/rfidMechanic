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
	//a function that updates the cards for texas hold em
	let playerCount = 2; //by default we're assuming the special case of less than 3 cards
	if(cards.length>2) playerCount = Math.ceil(cards.length/2); //the solution for any other case
	
	let cont = document.getElementById("holdEmGrid");
	
	cont.innerHTML="";
	
	for(let i=0;i<playerCount;i++){
		cont.innerHTML+="<div class='holdEmPlayer'>&#13<div class='holdEmProb'></div></div>&#13;"; //&#13 is CR
	}
	let players = document.getElementsByClassName("holdEmPlayer");
	
	let player = 0;
	
	for(let i=0;i<cards.length;i++){// we "deal" the cards into the divs
		
		if(player==playerCount) player = 0; //if we already dealt a card for each player, we want to go around one more time
		players[player].innerHTML+=toNames(cards[i]);
		player++;
		
		}
}

function updateHoldEmProb(cards){
	let playerCount = cards.length/2;
	let probsDivs = document.getElementsByClassName("holdEmProb");

	if(cards.length%2==0 && cards.length>2){
		let probs = holdEmProbability(cards,1000); //the second argument is the sample size - how many hands with given cards we want to simulate
		for(let i=0;i<playerCount;i++) probsDivs[i].innerHTML = probs[i].toFixed(2);
	}
	else{
		for(let i=0;i<probsDivs.length;i++) probsDivs[i].innerHTML = "...";
	}
}

function updateSingleCard(){
	let div = document.getElementById("singleCard-card");
	div.innerHTML = toNames(cards[cards.length-1]);
}

function updateCards(playerCount){
	//updates the amount of player divs and puts the translated card names inside of them
	cont = document.getElementById("equalDealGrid");
	cont.innerHTML="";
	for(let i=0;i<playerCount;i++){
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
			if(resp.length!=cards.length){  //the sample size for the simulation will be configurable later, so we don't want to repeat it,
										    // since it might last long enough to be annoying 
				cards=resp;
				updateCards(playerCount);
				updateHoldEm();
				updateSingleCard();
				updateHoldEmProb(cards);
			}
		});
}


playerSlider.oninput = function() {
	playerCount = this.value;
	var playerCounter = document.getElementById('playerCounter');
	playerCounter.innerHTML = playerCount;
	updateCards(playerCount);
}

clearCardsBtns = document.getElementsByClassName('clearCardsBtn');
for(let i=0;i<clearCardsBtns.length;i++){
	clearCardsBtns[i].onclick = function(){
		var xhr = new XMLHttpRequest();
		var url = "clear_cards";
		xhr.open("POST",url,true);
		
		xhr.send();
		
	}
}


getCards();

setInterval(getCards,1000)