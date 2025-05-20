// js/script.js

document.addEventListener('DOMContentLoaded', () => {
    const arquivo = window.location.pathname.split('/').pop()
    document.querySelectorAll('.menu a').forEach(link => {
      if (link.getAttribute('href') === arquivo) {
        link.classList.add('ativo')
      }
    })
  })
  
  const form = document.querySelector('form')
  if (form) {
    form.addEventListener('submit', e => {
      let valido = true
      ;['nome','email','mensagem'].forEach(name => {
        const f = form.querySelector(`[name="${name}"]`)
        if (!f.value.trim()) {
          f.style.borderColor = 'red'
          valido = false
        } else f.style.borderColor = '#ccc'
      })
      if (!valido) {
        e.preventDefault()
        alert('Preencha todos os campos!')
      }
    })
  }
  