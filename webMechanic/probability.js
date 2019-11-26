class Card{
	constructor(card){
		//constructor turns 'raw' card value into value (ace, 2,3...) and suit
		//card numbers go in CHSD order, so 1 to 13 are ace to king of clubs, 14 is the ace of hearts and so on 

		this.suit = Math.ceil(card/13)-1; //-1 for the arr indexes and for the suit*13 to work
		this.value = card - this.suit*13;
        
    }
};


function count(hand,value){
	//returns the amount of occurences of value in a hand
	let count = 0;
	for (i=0;i<hand.length;i++){
		
		if(hand[i].value==value)count++;
	}
	
	  return count;
}

/*
 * 
 * Functions like isPair check what kind of hand you passed them
 * They return false if it's not the right type of a hand
 * If the hand matches it returns a value that helps to determine how good it is 
 * (for pairs it will return the value of the cards that make up a pair)
 * 
 */

function isFlush(hand){
	  //checks if all cards in the hand are the same suit
	  let suit = hand[0].suit;
	  for(let i=1;i<hand.length;i++){
	    if(hand[i].suit!=suit) return false;
	  }
	  return true;
	}


//next three functions could be one, but gonna keep it that way for making the names more transparent

function isPair(hand){
	//checks if a given hand has a pair (it can be a full house too)

	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==2)
			return hand[i].value;
	}
	return false;
}


function isTrip(hand){
	//checks if a hand has a three of a kind (it can be a full house too)
	
	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==3)
			return hand[i].value;
	}
	return false;
}

function isQuad(hand){
	//checks if a hand has a four of a kind 
	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==4)
			return hand[i].value;
	}
	return false;
	
}

function isHouse(hand){
	//checks if the hand is a full house
	let a = isPair(hand);
	let b = isTrip(hand);
	if(a && b){
		if(a>b) return a;
		else return b;
		
	}
	else return false;
}

function isStraight(hand){
	hand.sort(function(a,b){
		return a.value-b.value;
	});
	let i=0; //by default we want to check all cards' values, unless there's a king and an ace 
	if(hand[0].value==1 && hand[hand.length-1].value==13) i=1; //check if there's a possibility for a straight with an ace and a king
	for(let i;i<hand.length-1;i++){ //checking if values are increasing by 1 each card, otherwise it's not a straight
		if(hand[i].value+1 != hand[i+1].value) return false;
	}
	return hand[hand.length-1];
	
	
}

function isStraightFlush(hand){
	let a = isStraight(hand);
	if(a && isFlush(hand)) return a;
	else return false;
}

function isTwoPair(hand){
	//checks if the hand has 2 pairs of same values
	let pairs = [];
	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==2 && !pairs.includes(hand[i].value))
			pairs.push(hand[i].value)
	}
	if(pairs.length==2){
		if(pairs[0]>pairs[1]) return pairs[0];
		else return pairs[1];
	}
	else return false;
}

function isRoyalFlush(hand){
	hand.sort(function(a,b){
		return a.value-b.value;
	});
	//if the hand is a straight flush that has both an ace and a king it's got to be a royal flush
	if(isStraightFlush(hand) && hand[0].value==1 && hand[hand.length-1].value==13) return true;
	else return false; 
}

function rateHand(hand){
	handValues=[];
	for(let i=0;i<5;i++) handValues.push(toValues(hand[i]));
	
}