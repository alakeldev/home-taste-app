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

// related with the delete profile button inside the chef profile 'my_profile.html'
function redirectToDeletePage() {
    window.location.href = '/chefs/deleteprofile/';
}

// related with the update profile button inside the chef profile 'my_profile.html'
function redirectToUpdatePage() {
    window.location.href = '/chefs/editprofile/';
}