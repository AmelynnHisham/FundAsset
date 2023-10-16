$(".addToCart").on("click", function (e) {
  var courseId = this.dataset.course;
  var fullSuite = this.dataset.full;

  var device = getDevice();
  updateCart(courseId, fullSuite, device);
});

function updateCart(courseId, fullSuite, device) {
  var url = "/updateCart/";
  var csrfToken = getToken("csrftoken");

  $.ajax({
    type: "POST",
    url: url,
    dataType: "json",
    data: {
      courseId: courseId,
      fullSuite: fullSuite,
      device: device,
    },
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrfToken,
    },
    success: (data) => {
      if (data.status == "success") {
        $("#SuccessModal").modal("show");
        $(`[data-course=${courseId}]`).prop("disabled", true);
        $(`[data-course=${courseId}]`).text("Added to Cart");
        $(`[data-full=True]`).prop("disabled", true);
        $(`[data-full=True]`).text("Added to Cart");
        cartCount();
      } else {
        $("#ErrorModal").modal("show");
      }
    },
    error: (error) => {
      $("#ErrorModal").modal("show");
    },
  });
}
