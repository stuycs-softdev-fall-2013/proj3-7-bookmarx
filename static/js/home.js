// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	    .sortable()
        .disableSelection();
    var formDropped = 0;

	var makeBookmark = function() {
	    if (formDropped != 1) {
		    var form = $('<form id="bookmark-maker"></form>')
		        .append($('<input placeholder="Title"></input>'))
		        .append($('<br>'))
		        .append($('<input placeholder="Link"></input>'))
		        .append($('<br>'))
		        .append($('<input type="submit"></input>'))
		        .insertAfter('#make-bookmark')
		    ;
		    formDropped = 1;
		} else {
		    $('#bookmark-maker').remove();
		    formDropped = 0;
		}
		// TODO: add ajax call to add bookmark to server
	}

	$("#make-bookmark").click(makeBookmark);
});
