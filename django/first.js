document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const messages = document.querySelectorAll('.messages');

    searchInput.addEventListener('input', function () {
        const query = searchInput.value.toLowerCase();

        messages.forEach(message => {
            const title = message.querySelector('h1').textContent.toLowerCase();
            const anons = message.querySelector('h3').textContent.toLowerCase();

            if (title.includes(query) || anons.includes(query)) {
                message.style.display = ''; // показываем элемент
            } else {
                message.style.display = 'none'; // скрываем элемент
            }
        });
    });
});
