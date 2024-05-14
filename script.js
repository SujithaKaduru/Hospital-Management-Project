document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('login-form');
  form.addEventListener('submit', function (event) {
      event.preventDefault();
      const username = form.elements.username.value;
      const password = form.elements.password.value;
      // Here you can add your login logic, for example, check if the username and password are correct
      // For this example, let's just show an alert saying "Successfully logged in"
      alert('Successfully logged in');
      // You can redirect the user to another page or perform any other actions here after successful login
  });
});
