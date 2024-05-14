document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('appointment-form');
    const successMessage = document.getElementById('success-message');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        
        // Here you can collect the form data
        const formData = new FormData(form);

        // Here you can send the form data to the server using AJAX or any other method
        // For this example, let's just show a success message
        successMessage.classList.remove('hidden');
        
        // You can reset the form if needed
        // form.reset();
    });
});
