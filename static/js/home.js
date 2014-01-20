// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	    .sortable()
        .disableSelection();
    var formDropped = false;

	var makeBookmark = function() {
	    if (formDropped) {
		    removeBookmarkMaker();
		} else {
		    var form = $('<form id="bookmark-maker"></form>')
		        .hide()
		        .append($('<input placeholder="Title"></input>'))
		        .append($('<br>'))
		        .append($('<input placeholder="Link"></input>'))
		        .append($('<br>'))
		        .append($('<a href="#" class="btn btn-success btn-xs">Create</a>'))
		        .insertAfter('#make-bookmark')
		        .slideDown();
		    ;
		    formDropped = true;
		}
		// TODO: add ajax call to add bookmark to server
	}

	var removeBookmarkMaker = function() {
	    var maker = $('#bookmark-maker');
		maker.slideUp(maker.remove);
		formDropped = false;
	}

	$("#make-bookmark").click(makeBookmark);
});
