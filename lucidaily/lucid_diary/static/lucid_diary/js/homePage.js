// Anim text

let screen_height = window.screen.height
let screen_width = window.screen.width

const getRandom = (min, max) => {
    return Math.floor(Math.random() * (max - min) + min)
}

 const animText = (text_class) => {

 	let colors = [
 		'rgb(255, 0, 0)',
 		'rgb(0, 0, 255)',
 		'rgb(0, 255, 0)',
 		'rgb(255, 255, 0)',
 		'rgb(0, 255, 255)',
 		'rgb(255, 0, 255)'
 	]
	
 	randomColor = colors[getRandom(0, colors.length)]

	if($(text_class).css('color') == randomColor) {
		
		currentIndex = randomColor.indexOf(randomColor)

		if (typeof (colors[currentIndex] + 1) == 'undefined') {
			randomColor = consols[currentIndex - 1]
		} else {
			randomColor = colors[currentIndex]
		}

	}
	$(text_class).css('color', randomColor)

}

setInterval(() => {animText('.getstart')}, 1000)

// Messages

$('#whatislucid').click(() => {
	Swal.fire({
		title: 'A lucid dream is a type of dream in which the dreamer becomes aware that they are dreaming while dreaming. During a lucid dream, the dreamer may gain some amount of control over the dream characters, narrative, or environment; however, this is not actually necessary for a dream to be described as lucid.',
		confirmButtonColor: 'rgb(33, 37, 41)'
	})
})

$('#howtostart').click(() => {
	Swal.fire({
		title: 'First you need blablabla; a couple of source; diary;',
		confirmButtonColor: 'rgb(33, 37, 41)'
	})
})

$('#whyuneed').click(() => {
	Swal.fire({
		title: 'Lucid diary are boosting your dream memory, you will getting random lucid dreams',
		confirmButtonColor: 'rgb(33, 37, 41)'
	})
})










