/**
 * Created by c0hb1rd on 2017/4/1.
 */
var rotation = 1;

jQuery.fn.rotate = function(degrees) {
    $(this).css({'transform' : 'rotate('+ degrees +'deg)'});
    return $(this);
};

setInterval(function () {
    $("#loading-img").rotate(rotation);
    rotation += 1;
}, 10);

$("#iframe").ready(function () {
    setTimeout(function () {
        $("#loading").css("display", "none")
    }, 500);
});


