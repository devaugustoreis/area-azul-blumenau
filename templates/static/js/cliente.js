function forcedReload() {
    setTimeout(function() {
        window.location.reload(true)
    }, 2000);
}


function deletarMensagem(botao) {
    botao.parentElement.remove()
}