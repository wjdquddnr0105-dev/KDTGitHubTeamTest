(function () {
    "use strict";
    const toggle = document.getElementById("smart-assistant-toggle");
    const drawer = document.getElementById("smart-assistant-drawer");
    const close = document.getElementById("smart-assistant-close");
    const tabs = Array.from(document.querySelectorAll("[data-assistant-tab]"));
    const panels = Array.from(document.querySelectorAll("[data-assistant-panel]"));

    function toggleSmartAssistant(forceOpen) {
        if (!toggle || !drawer) return;
        const open = typeof forceOpen === "boolean" ? forceOpen : !drawer.classList.contains("is-open");
        drawer.classList.toggle("is-open", open);
        drawer.setAttribute("aria-hidden", String(!open));
        toggle.setAttribute("aria-expanded", String(open));
        if (!open) toggle.focus();
    }

    function activateAssistantTab(tabName) {
        tabs.forEach((tab) => {
            const active = tab.dataset.assistantTab === tabName;
            tab.classList.toggle("is-active", active);
            tab.setAttribute("aria-selected", String(active));
        });
        panels.forEach((panel) => {
            const active = panel.dataset.assistantPanel === tabName;
            panel.classList.toggle("is-active", active);
            panel.hidden = !active;
        });
    }

    if (toggle) toggle.addEventListener("click", () => toggleSmartAssistant());
    if (close) close.addEventListener("click", () => toggleSmartAssistant(false));
    tabs.forEach((tab) => tab.addEventListener("click", () => activateAssistantTab(tab.dataset.assistantTab)));
    document.addEventListener("keydown", (event) => { if (event.key === "Escape") toggleSmartAssistant(false); });
    window.toggleSmartAssistant = toggleSmartAssistant;
    window.activateAssistantTab = activateAssistantTab;
}());
