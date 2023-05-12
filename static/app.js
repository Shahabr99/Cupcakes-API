"use strict";
const list = document.querySelector(".list");

const getCupcakes = async function () {
  const res = await axios.get("http://127.0.0.1:5000/api/cupcakes");

  const data = res.data.cupcake;

  for (let i = 0; i < data.length; i++) {
    list.insertAdjacentHTML("beforeend", `<li>${data[i].flavor}</li>`);
  }
};

getCupcakes();

$(".cupcake-form").on("submit", async function (e) {
  e.preventDefault();

  const flavor = $("#flavor").val();
  const size = document.querySelector("#size").value;
  const rating = $("#rating").val();
  const image = $("#image").val();

  await axios.post("/api/cupcakes", {
    flavor: flavor,
    size: size,
    rating: rating,
    image: image,
  });
});
