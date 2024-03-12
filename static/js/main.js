// event listener for alert messages if exists, set a timeout to hide it after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
    var messageElement = document.getElementById('msg-show');
    if (messageElement) {
        setTimeout(function () {
            messageElement.style.display = 'none';
        }, 5000);
    }
});