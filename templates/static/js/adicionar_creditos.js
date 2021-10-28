btnConfirmCredits = document.getElementById('btn-confirm-credits')

function btnAbleDisable() {
    if (totalCreditos > 0 && payment_method != '') btnConfirmCredits.disabled = false
    else {
        btnConfirmCredits.disabled = true
    }
}

/* Botões Adicionar Créditos */
let inputAumentoCustom = document.getElementById('aumento-creditos-custom')
let displayCreditos = document.querySelector('.total-creditos')
let saldoAtual = document.getElementById('saldo-atual').innerHTML
let displaySaldoFinal = document.querySelector('#saldo-final')

saldoAtual = saldoAtual.replace(/,/g, '.')
saldoAtual = parseFloat(saldoAtual)

let totalCreditos = 0
let saldoFinal = saldoAtual
displaySaldoFinal.innerHTML = `R$ ${saldoFinal.toFixed(2).replace(".", ',')}`

function aumentarCreditos(valor) {
    totalCreditos += valor
    displayCreditos.innerHTML = `R$ ${totalCreditos.toFixed(2).replace(".", ',')}`
    saldoFinal = saldoAtual + totalCreditos
    displaySaldoFinal.innerHTML = `R$ ${saldoFinal.toFixed(2).replace(".", ',')}`
    btnAbleDisable()
}

function reduzirCreditos(valor) {
    totalCreditos -= valor
    if (totalCreditos < 0) totalCreditos = 0
    displayCreditos.innerHTML = `R$ ${totalCreditos.toFixed(2).replace(".", ',')}`
    saldoFinal = saldoAtual + totalCreditos
    displaySaldoFinal.innerHTML = `R$ ${saldoFinal.toFixed(2).replace(".", ',')}`
    btnAbleDisable()
}

function aumentarCreditosCustom() {
    if (inputAumentoCustom.value < 0) inputAumentoCustom.value = 0
    if (inputAumentoCustom.value != '') {
        totalCreditos += parseFloat(inputAumentoCustom.value)
        displayCreditos.innerHTML = `R$ ${totalCreditos.toFixed(2).replace(".", ',')}`
        saldoFinal = saldoAtual + totalCreditos
        displaySaldoFinal.innerHTML = `R$ ${saldoFinal.toFixed(2).replace(".", ',')}`
        btnAbleDisable()
    }
}

function zerarCreditos() {
    totalCreditos = 0
    displayCreditos.innerHTML = `R$ ${totalCreditos.toFixed(2).replace(".", ',')}`
    saldoFinal = saldoAtual + totalCreditos
    displaySaldoFinal.innerHTML = `R$ ${saldoFinal.toFixed(2).replace(".", ',')}`
    btnAbleDisable()
}

/* Botões Método de Pagamento */
let btnCredito = document.getElementById('btn-credito')
let btnDebito = document.getElementById('btn-debito')
let btnPix = document.getElementById('btn-pix')

var payment_method = ''

function btnActive(botao1, botao2, botao3, pagamento) {
    botao2.classList.remove('btn-active')
    botao3.classList.remove('btn-active')
    botao1.classList.add('btn-active')
    payment_method = pagamento
    changeImgColor(botao1)
    btnAbleDisable()
}

msgCreditos = document.getElementById('msg-credito-adicionado')
msgCreditos.innerHTML = `Créditos adicionados à sua conta com sucesso!`

$(document).on('submit', '#add-credits-form', function(){ 
    $('#msg-credito-adicionado').html(`R$${totalCreditos.toFixed(2).replace(".", ',')} em créditos foram adicionados à sua conta com sucesso! Aguarde e a página será recarregada.`)

    $.ajax({
        type: 'POST',
        url: '',
        data: {
            value: totalCreditos,
            payment_method: payment_method,
            operation: 'Compra de Créditos',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        beforeSend:function(html) {
            setTimeout(function(){
                $("#div-msg-creditos").fadeIn()
            }, 3000);
        },
        success:function() {
            $("#div-msg-creditos").fadeIn()
            setTimeout(function() {
                $("#div-msg-creditos").fadeOut()
            }, 3000);
        }

    });

    return false
});
