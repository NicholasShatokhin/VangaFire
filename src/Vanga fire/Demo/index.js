var continaer = $('.map-container');

var columnWidth = 100;




function nextBlock() {
    $('.full').css({display : 'flex'});
    renderMaps(columnWidth);
}

function renderMaps(size) {
    i = 0;
    x = 0;
    y = 0;
    while (i < 9 * 9) {
        if (x === 9) {
            y++;
            x = 0;
        }
        continaer.append('<div class="block" id=' + y + "-" + x + '></div>');
        i++;
        x++;
    }
    $('.block').css({width: size, height: size * 0.65});

    $('#2-1').append('<div class="loading"></div><div class="warning">89%</div>');

    setTimeout(function () {
        $('#6-7').append('<div class="loading"></div><div class="warning">73%</div>')
    }, 15000)
}

$("body").on("click", '#next', function () {
   $("#first-block").hide(500, function () {
        nextBlock();
   });
});
$("body").on("click", '.loading', function () {
    $('#myModal').modal('show')
});