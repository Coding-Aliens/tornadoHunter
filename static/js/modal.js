document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('supportModal');
    const btn = document.getElementsByClassName('top-right-button')[0];
    const span = document.getElementsByClassName('close')[0];

    if (btn) {
        btn.onclick = function() {
            modal.style.display = 'block';
        }
    }

    if (span) {
        span.onclick = function() {
            modal.style.display = 'none';
        }
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
