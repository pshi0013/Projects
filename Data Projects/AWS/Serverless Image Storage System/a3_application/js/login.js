import { signIn, signUp, confirmSignUp } from './cognitoClient';

const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;

    try {
        const result = await signIn(email, password);
        console.log('Login success:', result);
        sessionStorage.setItem('idToken', result.IdToken);
        sessionStorage.setItem('accessToken', result.AccessToken);
        sessionStorage.setItem('refreshToken', result.RefreshToken);
        window.location.href = 'home.html';
    } catch (error) {
        alert('Login failed: ' + error.message);
    }
});

document.getElementById('register-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const firstName = document.getElementById('register-firstname').value;
    const lastName = document.getElementById('register-lastname').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;
    const passwordConfirm = document.getElementById('register-password-confirm').value;

    if (password !== passwordConfirm) {
        alert('Passwords do not match');
        return;
    }

    try {
        const result = await signUp(email, password, firstName, lastName);
        console.log('Registration success:', result);
        alert('Registration successful! Please check your email to verify your account.');
        // Show confirmation form
        container.classList.add("confirmation-mode");
    } catch (error) {
        alert('Registration failed: ' + error.message);
    }
});

document.getElementById('confirmation-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const email = document.getElementById('confirmation-email').value;
    const code = document.getElementById('confirmation-code').value;

    try {
        const result = await confirmSignUp(email, code);
        console.log('Confirmation success:', result);
        alert('Account confirmed! You can now sign in.');
        container.classList.remove("confirmation-mode");
        container.classList.remove("sign-up-mode");
    } catch (error) {
        alert('Confirmation failed: ' + error.message);
    }
});
