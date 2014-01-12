var gCount = 0;
var fCount = 0;
setTimeout(function() {
	fCount = 1;
}, 5000);
var signinCallback = function(authResult) {
	if (gCount == 0) {
		gCount++;
		return;
	}
	if (authResult['status']['signed_in']) {
		token = authResult.access_token;
		$.ajax({
			url: 'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token='+token,
			data: null,
			dataType: "jsonp"  
		}).success(getUserInfo);
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
		user_id : "g" + user_id
	});
}

window.fbAsyncInit = function() {
	FB.init({
		appId	: '511674402281522',
		status	: true, // check login status
		cookie	: true, // enable cookies to allow the server to access the session
		xfbml	: true	// parse XFBML
	});

	// Triggered when there is a change in user status, eg. login, logout
	FB.Event.subscribe('auth.authResponseChange', function(response) {
		console.log(fCount);
		console.log(response);
		if (fCount == 0) {
			return;
		}
		if (response.status === 'connected') {
			$().redirect(URL + 'login', {
				usern : 'PLACEHOLDER', // TODO add usern handling (requires db)
				user_id : "f" + response.authResponse.userID
			});
		} else {
			console.log("wat response.status was not connected, facebook");
		}
	});
};
