
// main function
$(function(){
	setCurrentMotionProfile();
	showCurrentOrientationImage();
	$("input[name=motion_profile]").on("click", setCurrentMotionProfile);
	$("input[name=actuator_orientation]").on("click", showCurrentOrientationImage);
	$("#input_data_form").submit(getActuatorsForInputData)
	$("#actuators_list_form").submit(getCodesFormsForActuators)
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

var getActuatorsForInputData = function(event) {
	event.preventDefault();	
	url = "/searchingEngine/ajax/get_actuators/"
	console.log("request to " + url)
	$.ajax({
		url: url,
		data: fetchInputData(),
		dataType: 'json',
		success: updateActuators
	});
}

var fetchInputData = function() {
	var motion_profile_name = $("input[name=motion_profile]:checked").val()
	var input_data = {
		'actuator_type'        : $("input[name=actuator_type]:checked").val(),
		'actuator_orientation' : $("input[name=actuator_orientation]:checked").val(),
		'step'                 : $("#expected_step_input").val(),
		'mass'                 : $("#expected_mass_input").val(),
		'distance_of_mass_x'   : $("#distance_of_mass_x").val(),
		'distance_of_mass_y'   : $("#distance_of_mass_y").val(),
		'distance_of_mass_z'   : $("#distance_of_mass_z").val(),
		'motion_profile'       : motion_profile_name,
		'motion_profile_params': getParamsObjectForMotionProfile(motion_profile_name)
	}
	return input_data
}

var updateActuators = function(data) {
	var list_div = $("#actuators_list_div")
	list_div.html('')

	var list_root = $('<ul/>').appendTo(list_div);
	$(data.actuators).each(function(key) {
	    console.log(data.actuators[key])
		var li = $('<li/>').appendTo(list_root);
		var a = $('<div/>').text(data.actuators[key].name).appendTo(li);
		var checkbox = $('<input />', {
		    type: 'checkbox',
		    id: 'checkbox_interested_' + data.actuators[key].id,
		    value: data.actuators[key].id }).appendTo(li);
		var label = $('<label />', {
		    'for': 'checkbox_interested_' + data.actuators[key].id,
		    text: 'Jestem zainteresowany' }).appendTo(li);
	})

	$("#actuators_list_button").show()
}

var getCodesFormsForActuators = function(event) {
	event.preventDefault();
	console.log("getCodesFormsForActuators called")
	url = "/searchingEngine/ajax/get_codes/"
	console.log("request to " + url)
	$.ajax({
		url: url,
		data: fetchCheckedActuators(),
		dataType: 'html',
		success: setCodes
	});
}

var fetchCheckedActuators = function() {
    console.log("fetchCheckedActuators called")

    data = {
        'input_data': fetchInputData(),
        'checked_actuators_ids': []
    }

    $("#actuators_list_div :checkbox:checked").each(function(){
        var raw_id = $(this).attr('id')
        var id = parseInt(raw_id.split("_")[2])
        data['checked_actuators_ids'].push(id)
    })

    console.log(data)
    return data
}

var setCodes = function(data) {
    $('#actuators_codes_div').html(data);
    $("#order_form").submit(sendOrder)
}

var sendOrder = function(event) {
	event.preventDefault();
	console.log("sendOrder called")
	url = "/searchingEngine/ajax/send_order/"
	console.log("request to " + url)
	$.ajax({
		url: url,
		data: getOrderData(),
		dataType: 'json',
		success: onOrderSent
	});
}

var getOrderData = function(){
    return {1:2}
}

var onOrderSent = function(data) {
    clearAll()
    alert("Wyslano zapytanie!")
}

var clearAll = function(){
    $("#actuators_list_button").hide()
    $('#actuators_codes_div').html('')
    $("#actuators_list_div").html('')
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
