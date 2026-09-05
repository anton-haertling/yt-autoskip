return (() => {
    const video = document.querySelector("video");
    const player = document.querySelector(".html5-video-player");

    const videoAd =
        video?.classList.contains("ad-showing") === true;

    const playerAd =
        player?.classList.contains("ad-showing") === true;

    const skipButton = document.querySelector(
        ".ytp-ad-skip-button, .ytp-ad-skip-button-modern"
    );

    const skipButtonVisible =
        skipButton !== null &&
        skipButton.offsetWidth > 0 &&
        skipButton.offsetHeight > 0;

    return Boolean(
        videoAd ||
        playerAd ||
        skipButtonVisible
    );
})();
