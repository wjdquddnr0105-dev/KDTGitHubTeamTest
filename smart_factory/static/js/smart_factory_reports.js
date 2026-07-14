(function () {
    "use strict";
    const rangeButtons = Array.from(document.querySelectorAll("#report-filters div button"));
    const exportButton = document.querySelector("#report-filters > button");

    rangeButtons.forEach((button) => button.addEventListener("click", function () {
        rangeButtons.forEach((item) => item.classList.remove("is-active"));
        button.classList.add("is-active");
    }));

    if (exportButton) {
        exportButton.addEventListener("click", function () {
            exportButton.textContent = "[ PREVIEW ONLY ]";
            window.setTimeout(() => { exportButton.textContent = "[ REPORT EXPORT ]"; }, 1400);
        });
    }
}());
