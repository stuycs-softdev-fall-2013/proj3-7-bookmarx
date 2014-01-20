// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	    .sortable()
        .disableSelection();

	var toggleBookmarkForm = function() {
        $('#bookmark-form').slideToggle();
	};

	var makeBookmark = function() {
        var inputs = $(".bookmark-form-input");
        console.log("bookmark!");
        $.post(URL + "action", {
                action : 'make-bookmark',
                // FIXME send user_id
                title : inputs[0].value,
                link : inputs[1].value
            }
        );
        toggleBookmarkForm();
	};

	$("#toggle-bookmark-form").click(toggleBookmarkForm);
	$("#make-bookmark").click(makeBookmark);
});
