$(function(){
	window.TTO = window.TTO || {};
    TTO.max_years = 20;
	TTO.init = function() {
		var val = TTO.getValue();
        var had_value = false;
		if (!val) {
			val = TTO.max_years; // Rang is 0-20
		} else {
            had_value = true;
        }
        console.log(had_value)
		TTO.setValue(val);
        $(".tto .tto_container .timeline.top").click(TTO.handleTopClick);
        $(".tto .tto_container .timeline.bottom").click(TTO.handleBottomClick);
        $(".tto_next.next_button").attr("disabled", "disabled");
        $(".reset_button").click(TTO.reset);
        TTO.enabled = true;
        if (had_value) {
            TTO.handleTopClick();
        }
	};
    TTO.reset = function() {
        TTO.enabled = true;
        TTO.setValue(TTO.max_years);
        $(".tto_next.next_button").attr("disabled", "disabled");
        $(".confirm_message").hide();
    }

	TTO.setValue = function (value) {
		$("#id_tto_rating").val(value);
        if (value == 0) {
            $(".tto .bottom .first_years").hide();
        } else {
            $(".tto .bottom .first_years").show();
        }
        $(".tto .bottom .first_years").css("width", (100.0 * value / TTO.max_years) + "%");

        $(".tto .bottom .second_years").css("width", (100.0 * (TTO.max_years - value)/TTO.max_years) + "%");
	};
	TTO.getValue = function() {
		return $("#id_tto_rating").val();
	};
    TTO.handleTopClick = function() {
        $(".confirm_message").show();
        $(".tto_next.next_button").removeAttr("disabled");
        TTO.enabled = false;
    };
    TTO.handleBottomClick = function() {
        if (TTO.enabled) {
            var val = TTO.getValue();
            val -= 0.5;
            if (val < 0) {
                val = 0;
            }
            TTO.setValue(val); 
        }
    };

	TTO.init();

});