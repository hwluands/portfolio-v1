// js/script.js

// Aguarda o carregamento completo do DOM antes de executar
document.addEventListener('DOMContentLoaded', () => {
    // Pega o nome do arquivo atual (ex: 'index.html')
    const arquivo = window.location.pathname.split('/').pop()
    // Percorre todos os links do menu
    document.querySelectorAll('.menu a').forEach(link => {
      // Se o href do link for igual ao arquivo atual, adiciona classe 'ativo'
      if (link.getAttribute('href') === arquivo) {
        link.classList.add('ativo')
      }
    })
  })
  
  // Seleciona o formulário, se existir na página
  const form = document.querySelector('form')
  if (form) {
    // Adiciona listener para validação ao enviar
    form.addEventListener('submit', e => {
      let valido = true
      // Campos obrigatórios para verificar: nome, email e mensagem
      ;['nome','email','mensagem'].forEach(name => {
        const f = form.querySelector(`[name="${name}"]`)
        // Se o campo estiver vazio, marca em vermelho e invalida
        if (!f.value.trim()) {
          f.style.borderColor = 'red'
          valido = false
        } else {
          // Se preenchido, retorna borda ao padrão
          f.style.borderColor = '#ccc'
        }
      })
      // Se algum campo for inválido, impede o envio e alerta
      if (!valido) {
        e.preventDefault()
        alert('Preencha todos os campos!')
      }
    })
  }
  