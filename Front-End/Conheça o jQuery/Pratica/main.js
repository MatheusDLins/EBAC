
$(document).ready(function() {
    // Exibe o formulário quando o botão "Nova tarefa" é clicado
    $('header button').click(function() {
        $('form').slideDown();
    });

    // Esconde o formulário quando o botão "Cancelar" é clicado
    $('#botao-cancelar').click(function() {
        $('form').slideUp();
    });

    // Adiciona a tarefa à lista quando o formulário é submetido
    $('form').submit(function(event) {
        event.preventDefault(); // Impede o comportamento padrão de envio do formulário

        // Pega o valor do input
        let tarefaNova = $('#nome-tarefa-nova').val();

        // Adiciona a tarefa à lista
        if (tarefaNova) {
            $('#lista-tarefas').append('<li>' + tarefaNova + '</li>');
        }

        // Limpa o campo de input
        $('#nome-tarefa-nova').val('');

        // Esconde o formulário
        $('form').slideUp();
    });

    // Marca uma tarefa como concluída ao clicar nela
    $('#lista-tarefas').on('click', 'li', function() {
        $(this).toggleClass('completed');
    });
});
