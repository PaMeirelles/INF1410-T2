// auth.ts
document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form") as HTMLFormElement;
    const registerForm = document.getElementById("register-form") as HTMLFormElement;

    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            // Add logic to handle login form submission using AJAX or fetch
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            // Add logic to handle register form submission using AJAX or fetch
        });
    }
});
