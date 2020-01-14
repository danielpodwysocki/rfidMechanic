var viewToggles = document.getElementsByClassName("menuitems");
for(i=0;i<viewToggles.length;i++){
	viewToggles[i].onclick = function(){
			for(i=0;i<viewToggles.length;i++){
				let view = document.getElementById(viewToggles[i].id.slice(5));
				view.style.display='none';
			}
			let view = document.getElementById(this.id.slice(5));
			view.style.display='block';
		};
		
}