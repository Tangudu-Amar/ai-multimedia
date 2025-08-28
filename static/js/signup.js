function validatePassword() {
    const password = document.getElementById("password").value;
    const errorDiv = document.getElementById("passwordError");

    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,16}$/;

    if (!regex.test(password)) {
        errorDiv.textContent = "Password must be 8–16 chars, include uppercase, lowercase, number, and symbol.";
        return false; // Prevent form submission
    }

    errorDiv.textContent = ""; // Valid password
    return true;
}

function checkPasswordStrength() {
    const password = document.getElementById("password").value;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,16}$/;
    const errorDiv = document.getElementById("passwordError");

    if (!regex.test(password)) {
        errorDiv.textContent = "Password must be 8–16 chars, include uppercase, lowercase, number, and symbol.";
    } else {
        errorDiv.textContent = "";
    }
}