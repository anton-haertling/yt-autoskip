const selectors = [
".ytp-ad-skip-button",
".ytp-ad-skip-button-modern",
".ytp-ad-skip-button-slot button",
".ytp-skip-ad-button",
"#ytp-skip-ad-button",
"button.ytp-ad-skip-button"
];

let button = null;

for (const selector of selectors) {
const elements = document.querySelectorAll(selector);

for (const element of elements) {
    const style = window.getComputedStyle(element);
    const rect = element.getBoundingClientRect();

    if (
        style.display !== "none" &&
        style.visibility !== "hidden" &&
        style.opacity !== "0" &&
        rect.width > 0 &&
        rect.height > 0
    ) {
        button = element;
        break;
    }
}

if (button) {
    break;
}


}

if (!button) {
return null;
}

const rect = button.getBoundingClientRect();

// Position des Browserfensters / Viewports
const offsetX = window.screenX - window.screenLeft;
let offsetY = window.screenY - window.screenTop;

const isFullscreen = document.fullscreenElement !== null;

if (!isFullscreen) {
    offsetY += 80
}



return {
x: rect.left,
y: rect.top,

width: rect.width,
height: rect.height,

right: rect.right,
bottom: rect.bottom,

center_x: rect.left + rect.width / 2,
center_y: rect.top + rect.height / 2,

offset_x: offsetX,
offset_y: offsetY,

selector: button.tagName + "." + button.className


};