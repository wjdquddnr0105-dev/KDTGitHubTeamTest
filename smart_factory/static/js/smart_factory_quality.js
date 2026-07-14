(function () {
    "use strict";
    const assets = Array.from(document.querySelectorAll("[data-quality-asset]"));
    const name = document.getElementById("quality-asset-name");
    const status = document.getElementById("quality-asset-status");

    function selectQualityAsset(assetId) {
        const selected = assets.find((asset) => asset.dataset.qualityAsset === assetId);
        if (!selected) return;
        assets.forEach((asset) => asset.classList.toggle("is-selected", asset === selected));
        if (name) name.textContent = assetId;
        if (status) status.textContent = selected.dataset.status || "상세 정보 없음";
    }

    assets.forEach((asset) => asset.addEventListener("click", () => selectQualityAsset(asset.dataset.qualityAsset)));
    window.selectQualityAsset = selectQualityAsset;
}());
