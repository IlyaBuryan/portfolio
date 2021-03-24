// Function for burger menu
let burger = document.getElementsByClassName("header_menu_burger")[0];
let nav = document.getElementsByClassName("header_menu_navbar")[0];
burger.onclick = function () {
    burger.classList.toggle("activated");
    nav.classList.toggle("activated");
}

// Curriculum hide
$('.hide-btn').on('click', function (event) {
    event.preventDefault();
    $('.main_section_study_text_list_item').toggleClass('hidden');
    $('.main_section_study_text_list_item_i').toggleClass('hidden');
    $('.main_section_study_hr').toggleClass('hidden');
    $('.main_section_study_hr').toggleClass('hidden');
    $('.main_flex').toggleClass('main_flex_activ');
    $('.main_done').toggleClass('main_done_activ');
})


