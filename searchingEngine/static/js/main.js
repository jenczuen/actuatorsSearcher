
// main function
$(function(){
	setCurrentMotionProfile();
	showCurrentOrientationImage();
	$("input[name=motion_profile]").on("click", setCurrentMotionProfile);
	$("input[name=actuator_orientation]").on("click", showCurrentOrientationImage);
	$("#actuator_model_form").submit(getActuators)
});

var showCurrentOrientationImage = function() {
	var img_container = $("#actuator_orientation_img_div")
	img_container.children().each(function(index) { 
		$(this).hide()
	})
	var orientation = $("input[name=actuator_orientation]:checked").val()
	var current_orientation_img = $("#actuator_orientation_img_" + orientation)
	current_orientation_img.show()
}

var setCurrentMotionProfile = function() {
	// hide all 
	$('#motion_profile_parameters').children().each(function(index) { 
		$(this).hide()
	})

	// show current
	var motion_profile = $("input[name=motion_profile]:checked").val()
	getParamsDivForMotionProfile(motion_profile).show()
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
	var motion_profile_name = $("input[name=motion_profile]:checked").val()
	var result = {
		'actuator_type'        : $("input[name=actuator_type]:checked").val(),
		'actuator_orientation' : $("input[name=actuator_orientation]:checked").val(),
		'expected_step'        : $("#expected_step_input").val(),
		'distance_of_mass_x'   : $("#distance_of_mass_x").val(),
		'distance_of_mass_y'   : $("#distance_of_mass_y").val(),
		'distance_of_mass_z'   : $("#distance_of_mass_z").val(),
		'motion_profile'       : motion_profile_name,
		'motion_profile_params': getParamsObjectForMotionProfile(motion_profile_name)
	}
	return result
}

var updateActuators = function(data) {
	var list_div = $("#actuators_list_div")
	list_div.html('')

	var list_root = $('<ul/>').appendTo(list_div);
	$(data.actuators).each(function(key) {
		var li = $('<li/>').appendTo(list_root);
		var a = $('<a/>').text(data.actuators[key].name).appendTo(li);
	})
}

var getParamsDivForMotionProfile = function(motion_profile) {
	return $("#" + motion_profile + "_parameters")
}

var getParamsObjectForMotionProfile = function(motion_profile) {
	var motion_profile_params_div = getParamsDivForMotionProfile(motion_profile)
	result = {}
	var inputs = motion_profile_params_div.find("input")
	inputs.each(function(key){
		result[inputs[key].name] = inputs[key].value
	}) 
	return result
}
