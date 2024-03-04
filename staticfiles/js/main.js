// Signup button on landing area home page
document.getElementById("mySignupButton").addEventListener("click", function () {
    window.open("/accounts/signup/", "_blank");
});

// view chefs button on home page inside about section
document.getElementById("myChefsButton").addEventListener("click", function () {
    window.open("/chefs/", "_blank");
});

// related with the delete profile button inside the chef profile 'my_profile.html'
function redirectToDeletePage() {
    window.location.href = '/chefs/deleteprofile/';
}

// related with the update profile button inside the chef profile 'my_profile.html'
function redirectToUpdatePage() {
    window.location.href = '/chefs/editprofile/'; 
}