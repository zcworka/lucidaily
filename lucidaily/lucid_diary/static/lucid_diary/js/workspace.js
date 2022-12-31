setInterval(() => {animText('.text-lucid')}, 1000)

$(".ul-list").ready(() => {
	window.location.assign("#list-begin")
})

$(".ul-list").ready(() => {
	$('.list-group-item').click(function() {
		let form = $(this).find('form')
		form.submit()
	})
})


