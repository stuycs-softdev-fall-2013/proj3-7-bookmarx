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
            .addClass("ui-state-default")
            .html($("<a></a>")
                .attr('href', inputs[1].value)
            )[0];
        console.log(bookmark);
        bookmark.firstChild.innerText = inputs[0].value;
        $(".untagged").append(bookmark);
	    var well = $(".untagged")[0].parentElement;
	    well.style.height = parseInt(well.style.height) + 28 + "px";
	};

  var removeBookmark = function(event) {
    var elt = event.target.parentElement;

    // Resize the well
    var well = elt.parentElement.parentElement;
    well.style.height = parseInt(well.style.height) - 28 + "px";

    // Remove the clicked item from the list 
    elt.parentElement.removeChild(elt);

    var bookmark_id = $(elt).find(".bookmark-id")[0].innerText;
    // AJAX in the haus
    $.post(URL + "action", {
        action : 'remove-bookmark',
        user_id : user_id,
        bookmark_id: bookmark_id
      }
    );
  }

	$("#toggle-bookmark-form").click(toggleBookmarkForm);
	$("#make-bookmark").click(makeBookmark);
	$(".remove-bookmark").click(removeBookmark);
});
