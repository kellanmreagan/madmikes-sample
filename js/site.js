(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Close" : "Menu";
    });
  }

  var links = document.querySelectorAll("[data-lightbox]");
  if (!links.length) return;

  var items = Array.prototype.map.call(links, function (a) {
    return { href: a.getAttribute("href"), title: a.getAttribute("title") || "" };
  });

  var box = document.createElement("div");
  box.className = "lightbox";
  box.setAttribute("role", "dialog");
  box.setAttribute("aria-modal", "true");
  box.innerHTML =
    '<button type="button" class="lb-close" aria-label="Close">&times;</button>' +
    '<button type="button" class="lb-prev" aria-label="Previous">&#8249;</button>' +
    '<img alt="">' +
    '<button type="button" class="lb-next" aria-label="Next">&#8250;</button>';
  document.body.appendChild(box);

  var img = box.querySelector("img");
  var index = 0;

  function show(i) {
    index = (i + items.length) % items.length;
    img.src = items[index].href;
    img.alt = items[index].title;
    box.classList.add("is-open");
  }

  function hide() {
    box.classList.remove("is-open");
    img.src = "";
  }

  links.forEach(function (a, i) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      show(i);
    });
  });

  box.querySelector(".lb-close").addEventListener("click", hide);
  box.querySelector(".lb-prev").addEventListener("click", function () { show(index - 1); });
  box.querySelector(".lb-next").addEventListener("click", function () { show(index + 1); });
  box.addEventListener("click", function (e) {
    if (e.target === box) hide();
  });
  document.addEventListener("keydown", function (e) {
    if (!box.classList.contains("is-open")) return;
    if (e.key === "Escape") hide();
    if (e.key === "ArrowLeft") show(index - 1);
    if (e.key === "ArrowRight") show(index + 1);
  });
})();
