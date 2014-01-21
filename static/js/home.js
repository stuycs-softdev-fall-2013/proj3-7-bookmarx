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
                user_id : user_id,
                title : inputs[0].value,
                link : inputs[1].value
            }
        );
        toggleBookmarkForm();

        // show new bookmark
        var bookmark = $("<li></li>")
            .addClass("ui-selector-all")
            .html($("<a></a>")
                .attr('href', inputs[1].value)
                .val(inputs[0].value)
            );
        $(".untagged").append(bookmark);
	};

	$("#toggle-bookmark-form").click(toggleBookmarkForm);
	$("#make-bookmark").click(makeBookmark);
});
