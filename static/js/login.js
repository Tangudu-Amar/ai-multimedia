document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        const flash = document.querySelector('ul');
        if (flash) flash.style.display = 'none';
    }, 4000); // 4 seconds
});

function togglePassword() {
    const pwd = document.getElementById("password");
    if (pwd.type === "password") {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }
}