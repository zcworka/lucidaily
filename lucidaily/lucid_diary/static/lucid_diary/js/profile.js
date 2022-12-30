$('head').append('<style>body {background: linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(255,154,0,1) 10%, rgba(208,222,33,1) 20%, rgba(79,220,74,1) 30%, rgba(63,218,216,1) 40%, rgba(47,201,226,1) 50%, rgba(28,127,238,1) 60%, rgba(95,21,242,1) 70%, rgba(186,12,248,1) 80%, rgba(251,7,217,1) 90%, rgba(255,0,0,1) 100%);}</style>');


// Anim text

window.location.assign("#profile-main")
  $('.img-fluid').click(() => {
    Swal.fire({
    title: 'Soon you will be able to upload your image!\n\nStay with us',
    confirmButtonColor: 'rgb(33, 37, 41)'
  })
  })

$('body').css('transition', '0.6s linear')




setInterval(() => {animText('.text-username')}, 1000)

let reversed = {
	'.text-username': false,
	'.text-email': false,
	'.text-joined_us': false
}

const kek_reverse = (text_class) => {
	$(text_class).click(() => {

	if(text_class == '.text-username') {
		reversed['.text-username'] ? reversed['.text-username'] = false : reversed['.text-username'] = true	
	}
	
	if(text_class == '.text-email') {
		reversed['.text-email'] ? reversed['.text-email'] = false : reversed['.text-email'] = true	
	}
	
	if(text_class == '.text-joined_us') {
		reversed['.text-joined_us'] ? reversed['.text-joined_us'] = false : reversed['.text-joined_us'] = true		
	}

	$(text_class).text($(text_class).text().split("").reverse().join(""))
	
	if(reversed['.text-username'] && reversed['.text-email'] && reversed['.text-joined_us']) {
		$('body').css('transform', 'scaleX(-1) rotate(720deg)')
		

	} else {
		$('body').css('transform', 'none')
	}

	})	

	
	
}

kek_reverse('.text-username')
kek_reverse('.text-email')
kek_reverse('.text-joined_us')

