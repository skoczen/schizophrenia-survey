$(function(){
	window.VAS = window.VAS || {};
	
	VAS.init = function() {
		var val = VAS.getValue();
		if (!val) {
			val = 50;
		}
		VAS.setValue(val);
		VAS.mouseIsDown = false;
		$(".vas .vas_container").mousedown(VAS.handleDown);
		$("body").mouseup(VAS.handleUp);
		$("body").mousemove(VAS.handleMove);
	}

	VAS.setValue = function (value) {
		var containerHeight = $(".vas .vas_container").height();
		$(".vas .filled_bar").height(containerHeight * (value / 100));
		$("#id_vas_rating").val(value);
	}
	VAS.getValue = function() {
		return $("#id_vas_rating").val();
	}
	VAS.handleDown = function(e) {
		VAS.mouseIsDown = true;
		VAS.handleClick(e)
	}
	VAS.handleUp = function(e) {
		VAS.mouseIsDown = false;
	}
	VAS.handleMove = function(e) {
		if (VAS.mouseIsDown) {
			VAS.handleClick(e);
		}
	}
	VAS.handleClick = function(e) {
        var eleTop = $(".vas .vas_container").offset().top;
        var height = $(".vas .vas_container").height();
        var yValue = height - (e.pageY - eleTop);
        percent = Math.round(100.0 * yValue / height);
        if (percent > 100) {
            percent = 100;
        } else { 
            if (percent < 0) {
                percent = 0;
            }
        }
        VAS.setValue(percent);
	}

	VAS.init();

})