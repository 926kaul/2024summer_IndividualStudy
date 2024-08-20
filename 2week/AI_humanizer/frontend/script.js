document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".LoginSignup_form__hG5dU");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const email = form.querySelector('input[type="email"]').value;
        const password = form.querySelector('input[type="password"]').value;

        // URL에서 쿼리 파라미터 추출
        const urlParams = new URLSearchParams(window.location.search);
        const responseType = urlParams.get('response_type');
        const clientId = urlParams.get('client_id');
        const redirectUri = urlParams.get('redirect_uri');
        const state = urlParams.get('state');
        const scope = urlParams.get('scope');

        const response = await fetch(`https://app.gptinf.kro.kr/login?response_type=${responseType}&client_id=${clientId}&redirect_uri=${redirectUri}&state=${state}&scope=${scope}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email, password: password }),
        });

        if (response.ok) {
            const data = await response.json();
            window.location.href = `/connect?response_type=${responseType}&client_id=${clientId}&redirect_uri=${redirectUri}&state=${state}&scope=${scope}`;
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    });
});

