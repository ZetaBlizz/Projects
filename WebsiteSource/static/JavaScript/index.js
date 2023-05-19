	function darkMode() {
		var element = document.getElementById('page');
	 	element.classList.toggle("dark-mode");
	 	var element = document.getElementById('navbar');
	 	element.classList.toggle("dark-mode");
	 	var element = document.getElementById('nightMode');
	 	element.classList.toggle("light-mode");
		var x = document.getElementById("resume").querySelectorAll('.pannel');
		for (let i = 0; i < x.length; i++){
			console.log(x[i].classList.toggle("dark-mode-panel"));
		}
	}

	function test() {
		var element = document.getElementById('page');
	 	element.classList.toggle("dark-mode");
	 	var element = document.getElementById('navbar');
	 	element.classList.toggle("dark-mode");
	 	var element = document.getElementById('nightMode');
	 	element.classList.toggle("light-mode");
		var x = document.getElementById("resume").querySelectorAll('.h');
		for (let i = 0; i < x.length; i++){
			console.log(x[i].classList.toggle("dark-mode-panel"));
		}
		
	}

	function test2() {
		const ids = [['page',0], ['navbar',0], ['nightMode',1], ['resume',2]];
		const mode = ['dark-mode', 'light-mode', 'dark-mode-panel']
		//long run check if ids have classes if not just toggle leave classes till last aka rearrange array
		for (let arraypos = 0; arraypos < ids.length; arraypos++){
			if (arraypos < 3) {
				document.getElementById(ids[arraypos][0]).classList.toggle(mode[ids[arraypos][1]]);
			} else {
				var x = document.getElementById(ids[arraypos][0]).querySelectorAll('.h');
				//if theres no common class have program create one 
				for (let i = 0; i < x.length; i++){
					console.log(x[i].classList.toggle(mode[ids[arraypos][1]]));
				}
			} 
		}
	}	