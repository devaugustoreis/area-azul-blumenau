/* Menu Lateral */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


/* Página "login" */
function deletarMensagem(botao) {
    botao.parentElement.remove()
}


function verifyLogin() {
    if ($('#username').val().length == 14 && $('#password').val().length > 4 ) document.getElementsByClassName('btn')[0].disabled = false
    else {
        document.getElementsByClassName('btn')[0].disabled = true
    }
}


$('#username').mask('000.000.000-00')


/* Página "esqueci_senha" */
var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/

function verifyEmail() {
    let validEmail = $("#esq_senha_input").val()
    if (!emailReg.test(validEmail) == false) document.getElementsByClassName('btn')[0].disabled = false
    else {
        document.getElementsByClassName('btn')[0].disabled = true
    }
}


/* Página "perguntas_frequentes" */
var acc = document.getElementsByClassName("accordion");

for (var i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        } 
    });
}
