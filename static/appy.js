"use strict";
const list = document.querySelector(".list");

class Cupcake {
  constructor(flavor, size, rating, image) {
    this.flavor = flavor;
    this.size = size;
    this.rating = rating;
    this.image = image;
  }

  async createCupcake() {
    const res = await axios.post("/api/cupcakes", {
      flavor: this.flavor,
      size: this.size,
      rating: this.rating,
      image: this.image,
    });
    console.log(res);
  }

  static async fetchAllCupcakes() {
    const res = await axios.get("http://127.0.0.1:5000/api/cupcakes");

    const result = res.data.cupcake;
    for (let i = 0; i < result.length; i++) {
      list.insertAdjacentHTML("beforeend", `<li>${result[i].flavor}</li>`);
    }
  }
}

$(".cupcake-form").on("submit", async function (e) {
  e.preventDefault();
  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image = $("#image").val();
  const cupcake = new Cupcake(flavor, size, rating, image);
  await cupcake.createCupcake();
});

Cupcake.fetchAllCupcakes();
