// signup btn inside landing area 'home' page
window.addEventListener('DOMContentLoaded', () => {
    let signupBtn = document.getElementById("mySignupButton");
    if (signupBtn) {
        signupBtn.addEventListener("click", function () {
            window.open("/accounts/signup/", "_blank");
        })
    }
});

// Chefs view btn inside about area 'home' page
window.addEventListener('DOMContentLoaded', () => {
    let chefsBtn = document.getElementById("myChefsButton");
    if (chefsBtn) {
        chefsBtn.addEventListener("click", function () {
            window.open("/chefs/", "_blank")
        })
    }
});

// alert message that appear for 5 seconds on a different user interactions
setTimeout(function () {
    let messageElement = document.getElementById('msg-show');
    messageElement.style.display = 'none';
}, 5000);