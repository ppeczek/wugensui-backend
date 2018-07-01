function preloadImages() {
  // preload images
  $("[data-preload-url]").each(function (i, x) {
    var el = $(x);
    var url = el.attr("data-preload-url");
    var image = new Image();
    el.toggleClass("preloading");
    // console.log("preloading");
    image.onload = function () {
      // console.log("preloaded", el);
      el.toggleClass("preloading");
      window.x = el;
      el.css({
        'background-image': 'url(' + url + ')',
        'background-size': 'cover',
        'background-repeat': 'no-repeat',
        'background-position': 'center center',
      });
      el.removeAttr('data-preload-url');
    };
    image.src = url;
  });
}

$(document).on('click', '[data-toggle="lightbox"]', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

$(document).ready(function () {
  preloadImages();
  $('[data-toggle="tooltip"]').tooltip();
});
