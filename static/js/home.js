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
        var inputs = $(".bookmark-form-input"),
            title = inputs[0].value,
            link = inputs[1].value;

        if (link.substring(0, 7) !== "http://") {
            link = "http://" + link;
        }
        if (!isUrl(link)) {
            alert("Please input a valid link");
            return;
        }

        var bookmark = $("<li></li>")
            .addClass("ui-state-default")
            .append($("<p></p>")
                .addClass("alignleft")
                .append($("<a></a>")
                    .text(title)
                    .attr('href', link)
                )
            );
        $(".untagged").append(bookmark)[0];

        // resize well to fit new element
        var well = $(".untagged")[0].parentElement;
        well.style.height = parseInt(well.style.height) + 28 + "px";

        $.post(URL + "action", {
                action : 'make-bookmark',
                user_id : user_id,
                title : title,
                link : link,
                dataType : "text"
            }
        ).done(function(d) {
            bookmark.append($("<span></span>")
                .addClass("bookmark-id")
                .text(d)
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

    var isUrl = function (s) {
        var regexp = /(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/;
        return regexp.test(s);
    }

    var bookmarkKeyPress = function(event) {
        if (event.which === 13) { // \n
            makeBookmark();
        }
    }

    $("#toggle-bookmark-form").click(toggleBookmarkForm);
    $("#make-bookmark").click(makeBookmark);
    $(".remove-bookmark").click(removeBookmark);
    $("#bookmark-title").keypress(bookmarkKeyPress);
    $("#bookmark-link").keypress(bookmarkKeyPress);

    $('.dropdown-menu').click(function(e) {
        if($(this).hasClass('dropdown-menu-form')) {
            e.stopPropagation();
        }
    });
});
