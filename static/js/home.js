// set up sortables as sortables
$(function() {
	var sortables = $(".sortable")
	    .sortable()
        .disableSelection();

	var toggleBookmarkForm = function() {
        $('#bookmark-form').slideToggle();
	};

	var makeBookmark = function() {
        // show new bookmark
        var inputs = $(".bookmark-form-input");
        console.log("bookmark!");
        var bookmark = $("<li></li>")
            .addClass("ui-state-default")
            .append($("<p></p>")
                .addClass("alignleft")
                .append($("<a></a>")
                    .attr('href', inputs[1].value)
                )
            );
        bookmark[0].firstChild.innerText = inputs[0].value;
        $(".untagged").append(bookmark)[0];

        // resize well to fit new element
	    var well = $(".untagged")[0].parentElement;
	    well.style.height = parseInt(well.style.height) + 28 + "px";

        $.post(URL + "action", {
                action : 'make-bookmark',
                user_id : user_id,
                title : inputs[0].value,
                link : inputs[1].value,
                dataType : "text"
            }
        ).done(function(d) {
            bookmark.append($("<span></span>")
                .addClass("bookmark-id")
                .html(d)
            );

            // Add the remove bookmark button
            bookmark.append($("<p></p>")
                .addClass("alignright")
                .append($("<a></a>")
                    .addClass("remove-bookmark")
                    .addClass("glyphicon")
                    .addClass("glyphicon-remove-circle")
                    .attr("href", "#")
                    .click(removeBookmark)
                )
            );
            toggleBookmarkForm();
        })
	};

  var removeBookmark = function(event) {
    var li = event.target.parentElement.parentElement;

    // Resize the well
    var well = li.parentElement.parentElement;
    well.style.height = parseInt(well.style.height) - 28 + "px";

    // Remove the clicked item from the list 
    li.parentElement.removeChild(li);

    var bookmark_id = $(li).find(".bookmark-id")[0].innerText;
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
