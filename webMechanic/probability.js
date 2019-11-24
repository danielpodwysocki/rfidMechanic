function toValues(card){
	//returns an array with 2 elements: value,suit
	arr=[];
	//card numbers go in CHSD order, so 1 to 13 are ace to king of clubs, 14 is the ace of hearts and so on 
	suit = Math.ceil(card/13)-1; //-1 for the arr indexes and for the suit*13 to work
	value = card - suit*13 -1;
	
	arr[0]=value;
	arr[1]=suit;
	
	return arr;
}


function isPair(hand){
	//checks if a given hand has a pair

	for(i=0;i<hand.length;i++){
		if(hand.filter(x => x==hand[i]).length>=2)
			return true;
	
	}
	return false;
}

function isTrip(){
	//checks if a hand has a three of a kind
}



function rateHand(hand){
	handValues=[];
	for(i=0;i<5;i++) handValues.push(toValues(hand[i]));
	
}