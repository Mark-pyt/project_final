function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + days*24*60*60*1000);
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for(let i=0; i < ca.length; i++) {
        let c = ca[i].trim();
        if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length));
    }
    return null;
}

function deleteCookie(name) {
    setCookie(name, "", -1);
}

function showCookieBanner() {
    if (!getCookie('cookieConsent')) {
        const banner = document.createElement('div');
        banner.id = 'cookie-banner';
        banner.innerHTML = `
            <p>Мы используем файлы cookie, чтобы улучшить ваш опыт на сайте. 
            <button id="accept-cookie">Принять</button></p>
        `;
        document.body.appendChild(banner);

        document.getElementById('accept-cookie').addEventListener('click', function() {
            setCookie('cookieConsent', 'accepted', 365);
            banner.style.display = 'none';
        });
    }
}

window.onload = function() {
    showCookieBanner();
};
