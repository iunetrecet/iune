function fullscreen(selector) {
    win = $(window);
    ele = $(selector);
    ele.width(win.width());
    ele.height(win.height());
};


$(window).load(function() {
    $(document).foundation();

    fullscreen('.full_screen');
});
