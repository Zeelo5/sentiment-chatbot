document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('chat-form');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const message = document.getElementById('user-message').value;

        try {
            const response = await fetch('/suggest', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: message })
            });

            const data = await response.json();
            responseDiv.textContent = data.message;
        } catch (error) {
            console.error('Error:', error);
        }
    });
});
