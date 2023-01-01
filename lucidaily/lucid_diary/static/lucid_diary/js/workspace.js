


setInterval(() => {animText('.text-lucid')}, 1000)
setInterval(() => {animText('.lucid-span')}, 1000)


$(".ul-list").ready(() => {
	window.location.assign("#list-begin")
})

$(".ul-list").ready(() => {
	$('.list-group-item').click(function() {
		let form = $(this).find('form')
		console.log(1)
		// form.submit()

		$.ajax({
			type: "POST",
        	data: {'safer': form.find('input').attr('value')},
        	url: "workspace/view",
        	success: function(data, response){
        		document.getElementsByClassName('note-view')[0].innerHTML = data
        	},
        	error: function (xhr, ajaxOptions, thrownError) {
        		document.getElementsByClassName('note-view')[0].innerHTML = xhr.responseText
      }
        });
	})
})


