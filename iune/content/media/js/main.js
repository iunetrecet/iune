function fullscreen(selector) {
    ele = $(selector);
    ele.hide()
    win = $(window);
    ele.width(win.width());
    ele.height(win.height());
    ele.show()
};


$(window).load(function() {
    fullscreen('.fullscreen');
    $(document).foundation();
});
