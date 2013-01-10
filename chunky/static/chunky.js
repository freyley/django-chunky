$(function() {

    var make_editable = function(index, el) {
        el = $(el);
        var data = el.html();
        var slug = el.data("chunky_slug");
        var url = el.data("chunky_url");
        var original_background;

        el.prepend("<a class='edit_chunk btn pull-right'>edit</a> ");
        el.find("a.edit_chunk").click(function() {
            edit_chunk(slug, data, url, el);
            return false;
        });

        el.find("a.edit_chunk").mouseover(function() {
            original_background = el.css("background");
            el.css("background", "yellow");
        })
        el.find("a.edit_chunk").mouseout(function() {
            el.css("background", original_background);
        })

    };


    var edit_chunk = function(slug, data, url, original) {

        $("#chunkytextarea").remove();

        var tmpl = _.template($("#chunky_form_template").html());
        var dom_obj = $(tmpl({ slug:slug, data:data }));
        dom_obj.dialog({
            modal: true,
            title: "Editing " + slug,
            width: 800,
            resizable: false
        });

        CKEDITOR.replace( 'chunkytextarea');

        dom_obj.find("button#save_chunk").click(function() {
            var csrf_token = $("input[name='csrfmiddlewaretoken']").val();
            var content = CKEDITOR.instances.chunkytextarea.getData();

            $.ajax({
                success: function() {
                    console.log("setting content of:", content);
                    original.html(content);
                    CKEDITOR.instances.chunkytextarea.destroy();
                    $(".ui-dialog").remove();
                    make_editable(0, original);
                },
                error: function(error) {
                    alert(error.responseText);
                },
                type: "POST",
                url: url,
                data: {
                    slug: slug,
                    content: content
                },
                headers: {
                    'X-CSRFToken' : csrf_token
                }
            });
            return false;
        });
    };


    var chunks = $("div[data-chunky_slug]");
    chunks.each(make_editable);




});
