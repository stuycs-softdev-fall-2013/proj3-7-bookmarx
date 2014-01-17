// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	sortables.sortable();
	sortables.disableSelection();

	var makeBookmark = function() {
		var sortables = $("#sortable")[0];
		var bookmark = document.createElement("li");
		name = $("#name")[0].value;
		link = $("#link")[0].value;
		bookmark.innerHTML = "<a href="+link+">"+name+"</a>";
		sortables.appendChild(bookmark);
		// TODO: add ajax call to add bookmark to server
	}

	$("#make-bookmark").click(makeBookmark);
});
