
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
		dataType: 'html',
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
    console.log("received matching actuators")
    $('#actuators_list_div').html(data);
	$("#actuators_list_button").show()
}

var getCodesFormsForActuators = function(event) {
	event.preventDefault();
	console.log("getCodesFormsForActuators called")
	url = "/searchingEngine/ajax/get_codes/"
	console.log("request to " + url)
	$.ajax({
		url: url,
		data: getDataForFetchingCodes(),
		dataType: 'html',
		success: setCodes
	});
}

var getDataForFetchingCodes = function() {
    var result = fetchCheckedActuators()
    result.calculated_data
    return result
}

var fetchCheckedActuators = function() {
    console.log("fetchCheckedActuators called")

    all_actuators_data = {
        'input_data': fetchInputData(),
        'checked_actuators_data': {}
    }

    $("#actuators_list_div :checkbox:checked").each(function(){
        var raw_id = $(this).attr('id')
        var id = parseInt(raw_id.split("_")[2])
        all_actuators_data['checked_actuators_data'][id] = {
            "torque": parseFloat($(this).siblings('input[name=torque]').val()),
            "speed": parseFloat($(this).siblings('input[name=speed]').val())
        }
    })

    console.log(all_actuators_data)
    return all_actuators_data
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
    orderData = {}
    orderData.email = $("#order_form_email").val(),
    orderData.items = []

    $( ".codes_list_entry" ).each(function( index ) {
        item = {}
        item.name = $(this).find(".actuator_name").text()
        item.size = $(this).find(".actuator_size").text()
        item.type = $(this).find(".actuator_type").text()
        item.carriage = $(this).find(".actuator_carriage").text()
        item.drive_shaft = $(this).find(".actuator_drive_shaft_selector").val()
        item.mounting_kit = $(this).find(".actuator_mounting_kit_selector").val()
        orderData.items.push(item)
    });

    console.log(orderData)
    return orderData
}

var onOrderSent = function(data) {
//    clearAll()
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
