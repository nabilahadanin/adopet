$("#profile-img").click(function() {
	$("#status-options").toggleClass("active");
});

$(".expand-button").click(function() {
  $("#profile").toggleClass("expanded");
	$("#contacts").toggleClass("expanded");
});

$("#status-options ul li").click(function() {
	$("#profile-img").removeClass();
	$("#status-online").removeClass("active");
	$("#status-away").removeClass("active");
	$("#status-busy").removeClass("active");
	$("#status-offline").removeClass("active");
	$(this).addClass("active");
	
	if($("#status-online").hasClass("active")) {
		$("#profile-img").addClass("online");
	} else if ($("#status-away").hasClass("active")) {
		$("#profile-img").addClass("away");
	} else if ($("#status-busy").hasClass("active")) {
		$("#profile-img").addClass("busy");
	} else if ($("#status-offline").hasClass("active")) {
		$("#profile-img").addClass("offline");
	} else {
		$("#profile-img").removeClass();
	};
	
	$("#status-options").removeClass("active");
});

function newMessage() {
	sender = $("#username").val();
	receiver = $("#username").val();
	message = $(".message-input input").val();
	if($.trim(message) == '') {
		return false;
	}
	
	$.ajax({
		url: "/send",
		method: "POST",
		data : {
			sender: sender,
			receiver: receiver,
			message: message,
		},
        success : function(json) {
            console.log("Message " + message+ " from " + sender + " to " + receiver + "sent successfully.");
        }
    })
};

function openChat(username) {
	var i, x;
	x = document.getElementsByClassName("hideAble");
	for (i = 0; i < x.length; i++) {
	  x[i].style.display = "none";
	  x[i].classList.remove("active");
	}
	document.getElementById(username).style.display = "block";
	document.getElementsById(username).className = "active";
}

$('.submit').click(function() {
  newMessage();
  location.reload();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    newMessage();
    return false;
  }
});
