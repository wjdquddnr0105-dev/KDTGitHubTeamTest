(function () {
    "use strict";
    const button = document.querySelector("#threshold-settings button");
    const inputs = Array.from(document.querySelectorAll("#threshold-settings input"));

    if (!button) return;

    button.addEventListener("click", function () {
        button.textContent = "[ SAVED ]";
        inputs.forEach((input) => input.classList.add("is-saved"));
        window.setTimeout(() => { button.textContent = "[ APPLY SETTINGS ]"; }, 1400);
    });
}());
