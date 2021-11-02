function change_navbar_icon_caption(win) {
    if (win.width() >= 992) {
        $('span#cart-title').text('');
        $('span#profile-title').text('');
    } else {
        $('span#cart-title').text('Корзина');
        $('span#profile-title').text('Аккаунт');
    }
}

$(document).ready(function () {
    $("[data-link]").click(function () {
        window.location.href = $(this).attr("data-link");
        return false;
    });
});

$(window).on("load", function () {
    change_navbar_icon_caption($(window));
});

$(window).on('resize', function () {
    change_navbar_icon_caption($(this));
});

$(document).on('show.bs.dropdown', function (e) {
    var dropdown = $(e.target).find('.dropdown-menu#genres-dd');

    dropdown.appendTo('body');
    $(this).on('hidden.bs.dropdown', function () {
        dropdown.appendTo(e.target);
    })
});

$('form.quant-form>select#id_quantity').on('change', (event) => {
    $(event.target).closest('.quant-form').submit();
});

$('button#create-order-button').on('click', () => {
    if ($('#main-container').children().length > 2) {
        window.location.href = "/orders/create";
    } else {
        $('#cart-is-empty').show();
    }
});

// $('button#tech-sup-link').on('click', () => {
//     if (user_auth) {
//         window.location.href = chat_link;
//     } else {
//         $('#not-log').show();
//     }
// });

$('#close-alert-cart-empty').on('click', (event) => {
    $(event.target).closest('div.alert').hide();
});