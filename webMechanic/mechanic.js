//A script that pulls a json file and then adds divs containg information about players' hands

cards=[]

function updateCards(){
	//the ip can be hardcoded, because the app is hosted on the rapsberry pi access point
	//right now it's localhost for testing purposes
	fetch("http://127.0.0.1:8080/getcards")
		.then(resp=>resp.json())
		.then(resp => {
			console.log(resp);
		});
}

updateCards()
console.log(cards)