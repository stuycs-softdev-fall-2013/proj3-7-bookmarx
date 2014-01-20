// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	    .sortable()
        .disableSelection();

	var toggleBookmarkForm = function() {
        $('#bookmark-form').slideToggle();
	}

	$("#make-bookmark").click(toggleBookmarkForm);
});
