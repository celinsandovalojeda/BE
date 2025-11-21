document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('login-form');
  if (form) {
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;

      try {
        const res = await fetch('/api/token/', {
          method: 'POST',
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ username, password })
        });

        if (!res.ok) throw "Error";

        const data = await res.json();
        localStorage.setItem('access', data.access);
        localStorage.setItem('refresh', data.refresh || '');

        window.location = '/';
      } catch (err) {
        const errEl = document.getElementById('login-error');
        if (errEl) {
          errEl.innerText = "Credenciales inválidas";
          errEl.style.display = "block";
        }
      }
    });
  }
});

async function apiFetch(url, method = "GET", body = null) {
  const token = localStorage.getItem("access");
  const headers = { "Content-Type": "application/json" };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const resp = await fetch(url, {
    method,
    headers,
    body: body ? JSON.stringify(body) : null
  });

  if (resp.status === 401) {
    // token expired or not authorized - redirect to login
    window.location = '/login/';
  }
  return resp;
}
