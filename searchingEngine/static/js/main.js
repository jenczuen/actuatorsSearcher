
// main function
$(function(){
	setCurrentMotionProfile();
	$("input[name=motion_profile]").on("click", setCurrentMotionProfile);
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


