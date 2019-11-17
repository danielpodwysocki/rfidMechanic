var viewToggles = document.getElementsByClassName("menuitems");
for(i=0;i<viewToggles.length;i++){
	console.log();
	viewToggles[i].onclick = function(){
			for(i=0;i<viewToggles.length;i++){
				let view = document.getElementById(viewToggles[i].id.slice(5));
				view.style.display='none';
			}
			console.log(this.id);
			let view = document.getElementById(this.id.slice(5));
			view.style.display='block';
		};
		
}