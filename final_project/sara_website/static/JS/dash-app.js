window.onload = () => {
  // Selecting carousel or description
  const carousel_selector = document.getElementById("ca");
  const description_selector = document.getElementById("dc");

  const carousel_form = document.getElementById("carousel-add");
  const description_form = document.getElementById("description-add");

  //By default only carousel showing
  carousel_selector.style.backgroundColor = "#220935";
  description_form.style.display = "none";

  description_selector.addEventListener("click", () => {
    carousel_selector.style.backgroundColor = "#321B44";
    description_selector.style.backgroundColor = "#220935";

    description_form.style.display = "block";
    carousel_form.style.display = "none";
  });

  carousel_selector.addEventListener("click", () => {
    carousel_selector.style.backgroundColor = "#220935";
    description_selector.style.backgroundColor = "#321B44";

    description_form.style.display = "none";
    carousel_form.style.display = "block";
  });

  //Navbar functionality
  const abt_btn = document.getElementById("dash-abt");
  const pt_btn = document.getElementById("dash-pt");
  const wrt_btn = document.getElementById("dash-wrt");

  const abt_dash = document.getElementById("abt-me-dash");
  const pt_dash = document.getElementById("pt-dash");
  const wrt_dash = document.getElementById("wrt-dash");

  const at_indi_1 = document.getElementById("abt-dash-indi-1");
  const at_indi_2 = document.getElementById("abt-dash-indi-2");
  const pt_indi_1 = document.getElementById("pt-dash-indi-1");
  const pt_indi_2 = document.getElementById("pt-dash-indi-2");
  const wrt_indi_1 = document.getElementById("wrt-dash-indi-1");
  const wrt_indi_2 = document.getElementById("wrt-dash-indi-2");

  at_indi_1.style.backgroundColor = "#321B44";
  at_indi_2.style.backgroundColor = "#321B44";
  pt_indi_1.style.backgroundColor = "#161224";
  pt_indi_2.style.backgroundColor = "#161224";
  wrt_indi_1.style.backgroundColor = "#161224";
  wrt_indi_2.style.backgroundColor = "#161224";

  abt_dash.style.display = "grid";
  pt_dash.style.display = "none";
  wrt_dash.style.display = "none";

  abt_btn.addEventListener("click", () => {
    at_indi_1.style.backgroundColor = "#321B44";
    at_indi_2.style.backgroundColor = "#321B44";
    pt_indi_1.style.backgroundColor = "#161224";
    pt_indi_2.style.backgroundColor = "#161224";
    wrt_indi_1.style.backgroundColor = "#161224";
    wrt_indi_2.style.backgroundColor = "#161224";

    abt_dash.style.display = "grid";
    pt_dash.style.display = "none";
    wrt_dash.style.display = "none";
  });
  pt_btn.addEventListener("click", () => {
    at_indi_1.style.backgroundColor = "#161224";
    at_indi_2.style.backgroundColor = "#161224";
    pt_indi_1.style.backgroundColor = "#321B44";
    pt_indi_2.style.backgroundColor = "#321B44";
    wrt_indi_1.style.backgroundColor = "#161224";
    wrt_indi_2.style.backgroundColor = "#161224";

    abt_dash.style.display = "none";
    pt_dash.style.display = "grid";
    wrt_dash.style.display = "none";
  });
  wrt_btn.addEventListener("click", () => {
    at_indi_1.style.backgroundColor = "#161224";
    at_indi_2.style.backgroundColor = "#161224";
    pt_indi_1.style.backgroundColor = "#161224";
    pt_indi_2.style.backgroundColor = "#161224";
    wrt_indi_1.style.backgroundColor = "#321B44";
    wrt_indi_2.style.backgroundColor = "#321B44";

    abt_dash.style.display = "none";
    pt_dash.style.display = "none";
    wrt_dash.style.display = "grid";
  });

  //Modals Handling
};
