function adjustWrap() {
    var distance = $(window).height() - $('nav').outerHeight();
    $('#wrap').css('top', distance);
};


$(window).load(function() {
    $('.grayscale').BlackAndWhite({
        hoverEffect: true,
        responsive: true,
        inverHoverEffect: false,
        speed: 200
    });

    adjustWrap();
});
