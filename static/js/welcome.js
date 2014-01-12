var count = 0;
var signinCallback = function(authResult) {
	if (count != 0) {
		if (authResult['status']['signed_in']) {
			token = authResult.access_token;
			$.ajax({
				url: 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token='+token,
				data: null,
				dataType: "jsonp"  
			}).success(getUserInfo);
		}
	} else {
		count++;
	}
}

var getUserInfo = function() {
	$.ajax({
		url: 'https://www.googleapis.com/oauth2/v1/userinfo?access_token='+token,
		data: null,
		dataType: "jsonp"
	}).success(redirectUser);
}

var redirectUser = function(user) {
	var user_id = user.id;
	$().redirect(URL + 'login', {
		usern : 'PLACEHOLDER', // TODO add usern handling (requires db)
		user_id : user_id
	});
}
