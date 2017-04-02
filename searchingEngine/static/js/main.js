
// main function
$(function(){
	setCurrentMotionProfile();
	$("input[name=motion_profile]").on("click", setCurrentMotionProfile);

	//$("#actuator_model_button").on("click", getActuators);

	$("#actuator_model_form").submit(getActuators)
});

var setCurrentMotionProfile = function() {
	// hide all 
	$('#motion_profile_parameters').children().each(function(index) { 
		$(this).hide()
	})

	// show current
	var motion_profile = $("input[name=motion_profile]:checked").val()
	var current_params_id = "#" + motion_profile + "_parameters"
	$(current_params_id).show()
};

var getActuators = function(event) {
	event.preventDefault();	
	url = "/searchingEngine/ajax/get_actuators/"
	console.log("request to " + url)
	$.ajax({
		url: url,
		data: getInputsAsObject(),
		dataType: 'json',
		success: updateActuators
	});
}

var getInputsAsObject = function() {
	var result = {
		'model': "data"
	}
	return result
}

var updateActuators = function(data) {
	console.log(data)
	var list_div = $("#actuators_list_div")
	list_div.html('')

	var list_root = $('<ul/>').appendTo(list_div);
	$(data.actuators).each(function(key) {
		var li = $('<li/>').appendTo(list_root);
		var a = $('<a/>').text(data.actuators[key].name).appendTo(li);
		console.log(a)
	})
}


