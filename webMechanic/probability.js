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

function highCard(arr){
	//return the highest card in arr (doesn't inform about ties in any way!)
	arr.sort(function(a,b){
		return a.value-b.value;
	});
	return arr[arr.length-1];
}

/*
 *
 * Functions like isPair check what kind of hand you passed them
 * They return false if it's not the right type of a hand
 * If the hand matches it returns a value that helps to determine how good it is
 * (for pairs it will return the value of the cards that make up a pair + highest non pair card divided by 10)
 *
 */

function isFlush(hand){
	  //checks if all cards in the hand are the same suit
	  let suit = hand[0].suit;
	  for(let i=1;i<hand.length;i++){
	    if(hand[i].suit!=suit) return false;
	  }
	  return highCard(hand);
	}


//next three functions could be one, but gonna keep it that way for making the names more transparent

function isPair(hand){
	//checks if a given hand has a pair (it can be a full house too)

	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==2){
			let filtered = hand.filter(function(value, index, arr){
	    return value != hand[i];
			});

			return hand[i].value + highCard(filtered).value/10;
		}

	}
	return false;
}


function isTrip(hand){
	//checks if a hand has a three of a kind (it can be a full house too)

	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==3)
		{
			let filtered = hand.filter(function(value, index, arr){
	    return value != hand[i];
			});

			return hand[i].value + highCard(filtered)/10;
		}
	}
	return false;
}

function isQuad(hand){
	//checks if a hand has a four of a kind
	for(let i=0;i<hand.length;i++){
		if(count(hand,hand[i].value)==4){
			let filtered = hand.filter(function(value, index, arr){
	    return value != hand[i];
			});

			return hand[i].value + highCard(filtered)/10;
		}
	}
	return false;

}

function isHouse(hand){
	//checks if the hand is a full house
	let a = isPair(hand);
	let b = isTrip(hand);
	if(a && b){
		if(a>b) return a+b/10;
		else return b+a/10;

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
		if(pairs[0]>pairs[1]) return pairs[0]+pairs[1]/10;
		else return pairs[1]+pairs[0]/10;
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
	//returns a float. the higher it is the better the hand
	//still need to tweak it to incorporate kicker values in the evaluation of a hand

	//going from high to low to avoid giving too low a rating (a straight flush is also a straight, but it should be given a higher number)
	let rateFuncs = [isRoyalFlush, isStraightFlush, isQuad, isHouse, isFlush, isStraight, isTrip, isTwoPair, isPair];
	for(let i=0;i<rateFuncs.length){
		if(let r = rateFuncs[i](hand)){
			//length -i *14, so a high card value (up to 13 for the king) doesn't override a hand being better (so that a pair of kings isn't better than trip twos
			//then we add the value returned by a func from rateFuncs array, which is a float (higher means better hand)
			return (rateFuncs.length-i)*14+r;
		}
	}

}


fucntion bestHand(hands){
	//returns index of best hand out of an array of hands (a hand is an array of card objects) or -1 if it's a tie
	let ratings = []; 	//an array of hand ratings, indexes matching their counterparts in hands arr
	for(let i=0;i<hands.length;i++) ratings.push(rateHand(hands[i]));
	ratings.sort(function(a,b){
		return a-b;
	});
	//if there's no tie, return hightest rating, three way-tie is so improbable that we're going to discard such a possibility for now
	if(ratings[ratings.length-1]!=ratings[ratings.length-2]) return ratings[ratings.length-1];
	else return -1;
}

function toHands(cardsRaw, playerCount){
	//returns an array of hands, takes an array of raw card values(in the format given by /get_cards) and an amount of players as args
	let cards = []; //array of card objects
	let hands = []; //array of hands (each hand is an array of card objects)
	for(let i=0;i<cardsRaw.length;i++) cards.push(new Card(cardsRaw[i])); //convert raw card values to card objects
	for(let i=0;i<playerCount;i++) hands.push(new Array()); //fill the hands arr with as many arrs as there are players

	let player = 0;
	for(let i=0;i<cards.length;i++){
		if(player==playerCount) player = 0;
		hands[player].append(cards[i]);
		player++;
	}
	return hands;
}
