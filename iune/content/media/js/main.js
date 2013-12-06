$(document).foundation();

function fullscreen(selector) {
    win = $(window);
    ele = $(selector);
    ele.width(win.width());
    ele.height(win.height());
};


$(window).load(function() {
    $('.grayscale').BlackAndWhite({
        hoverEffect: true,
        responsive: true,
        inverHoverEffect: false,
        speed: 200
    });

    fullscreen('.full_screen');
});
