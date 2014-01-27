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
                .append($("<input>")
                    .attr('type', 'checkbox')
                    .addClass("should-tag")
                ).append($("<a></a>")
                    .text("  " + title)
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

        // AJAX in the haus
        var bookmark_id = $(li).find(".bookmark-id")[0].innerText;
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

    var tagAction = function(event) {
        var bookmarks = $(".ui-state-default");
        for (var i = 0; i < bookmarks.length; i++) {
            var checkbox = $(bookmarks[i]).find(".should-tag")[0];
            if (checkbox.checked) {
                var tags = $("#tag");
                for (var j = 0; j < tags.length; j++) {
                    var checkbox = $(tags[j]).find(".should-use-tag")[0];
                    if (checkbox.checked) {
                        event.data.action(bookmarks[i], tags[j]);
                    }
                }
            }
        }

        // make new tag
        if (event.data.action === addTag) {
            var tag_name = $("#new-tag-name").val().trim();
            if (tag_name) {
                // add tag to DOM
                var well = $("<div></div>")
                    .addClass("tag well")
                    .append($("<h3></h3>")
                        .text(tag_name)
                    ).append($("<ul></ul>")
                        .addClass("sortable")
                        .sortable()
                        .disableSelection()
                    )
                    .appendTo($("#content"));

                // add appropriate bookmarks
                for (var i = 0; i < bookmarks.length; i++) {
                    if ($(bookmarks[i]).find(".should-tag")[0].checked) {
                        addTag(bookmarks[i], well);
                    }
                }

                // add tag to db
                $.post(URL + "action", {
                    action : "make-tag",
                    tag_name : tag_name,
                    user_id : user_id
                }).done(function(d) {
                    well.append($("<span></span>")
                        .css('visibility', 'hidden')
                        .addClass("tag-id")
                        .text(d)
                    );
                });
            }
        } else if (event.data.action === removeTag) {
            // remove empty tags ?
        }

        var checkboxes = $(".should-tag");
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = false;
        }
        var checkboxes = $(".should-use-tag");
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = false;
        }
        $("#drop-tag-form").click();
    }

    var addTag = function(bookmark, tag) {
        // add to db
        var bookmark_id = $(bookmark).find(".bookmark-id").text();
        var tag_id = $(tag).find(".tag-id").text();
        $.post(URL + "action", {
            action : "add-tag",
            bookmark_id : bookmark_id,
            tag_id : tag_id
        }).done(function(){console.log("add tag");});
        
        // if bookmark was untagged, remove from untagged
        var untaggeds = $("untagged");
        for (var i = 0; i < untaggeds.length; i++) {
            var idnum = $(untaggeds[i]).find(".bookmark-id").text();
            if (tag_id === idnum) {
                $(untaggeds[i]).remove();
                break;
            }
        }

        // add to DOM
        var tags = $(".tag");
        for (var i = 0; i < tags.length; i++) {
            var idnum = $(tags[i]).find(".tag-id").innerText;
            if (bookmark_id === idnum) {
                $(tags[i]).append(bookmark);
                break;
            }
        }
    }

    var removeTag = function(bookmark, tag) {
        // add to db
        var bookmark_id = $(bookmark).find(".bookmark-id").text();
        var tag_id = $(tag).find(".tag-id").text();
        $.post({
            action : "remove-tag",
            bookmark_id : bookmark_id,
            tag_id : tag_id
        });
        
        // remove from DOM
        var tags = $(".tag");
        for (var i = 0; i < tags.length; i++) {
            var idnum = $(tags[i]).find(".tag-id").innerText;
            if (tag_id === idnum) {
                var bookmarks = $(tags[i]).find(".ui-state-default");
                for (var i = 0; i < bookmarks.length; i++) {
                    var idnum = $(bookmarks[i]).find(".bookmark-id").text();
                    if (bookmark_id === idnum) {
                        $(bookmarks[i]).remove();
                        break;
                    }
                }
                break;
            }
        }

        // if bookmark is now untagged, add to untagged
        var bookmark_ids = $(".bookmark-id").text();
        var is_tagged = false;
        for (var i = 0; i < bookmark_ids.length; i++) {
            if (bookmark_ids[i] === bookmark_id) {
                is_tagged = true;
                break;
            }
        }
        if (!is_tagged) {
            $(".untagged").append(bookmark);
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
    $('#tag-add').bind('click', {action : addTag}, tagAction);
    $('#tag-remove').bind('click', {action : removeTag}, tagAction);
});
