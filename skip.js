return (() => {
    const selectors = [
        ".ytp-ad-skip-button",
        ".ytp-ad-skip-button-modern",
        ".ytp-skip-ad-button"
    ];

    for (const selector of selectors) {
        const element = document.querySelector(selector);

        if (!element) {
            continue;
        }

        const rect = element.getBoundingClientRect();
        const style = window.getComputedStyle(element);

        const visible =
            rect.width > 0 &&
            rect.height > 0 &&
            style.display !== "none" &&
            style.visibility !== "hidden";

        if (visible) {
            return true;
        }
    }

    return false;
})();
