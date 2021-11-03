var chosenCar = ''

/* Botões Tipo de Veículo e Veículo */
let vehicleTypeButtons = document.getElementsByClassName('btn-vehicle-type') 

let allVehicles = document.getElementsByClassName('btn_vehicle_plate')
let cars = document.getElementsByClassName('btn-car')
let motos = document.getElementsByClassName('btn-moto')
let others = document.getElementsByClassName('btn-other')

/* Botões Adicionando Tempo */
let displayTimeValue1 = document.querySelector('#estacionar-value1')
let displayTimeValue2 = document.querySelector('#estacionar-value2')
let displayTempo = document.querySelector('.total-tempo')
let displayValue = document.querySelector('.total-value')

let btnEstacionar = document.getElementById('btn-estacionar')

let totalTempo = 0
let totalValue = 0
let valorVeiculo1 = 0
let valorVeiculo2 = 0
let tipoVeiculo = ''


function btnActive(botao) {
    btnEstacionar.disabled = true
    chosenCar = botao.id
    totalTempo = 0
    totalValue = 0
    displayTempo.innerHTML = `${totalTempo}min`
    displayValue.innerHTML = `R$ ${totalValue.toFixed(2)}`
    for (let vehicle of allVehicles) {
        vehicle.classList.remove('btn-active')
    }
    botao.classList.add('btn-active')
    resetColor()
    if (botao.classList.contains('btn-car') || botao.classList.contains('btn-other')) {
        valorVeiculo1 = 1.50
        valorVeiculo2 = 3
        tipoVeiculo = 'car or other' 
        displayTimeValue1.innerHTML = `R$ ${valorVeiculo1.toFixed(2).replace(".", ',')}`
        displayTimeValue2.innerHTML = `R$ ${valorVeiculo2.toFixed(2).replace(".", ',')}`
    }
    if (botao.classList.contains('btn-moto')) {
        valorVeiculo1 = 0.75
        valorVeiculo2 = 1.5
        tipoVeiculo = 'moto' 
        displayTimeValue1.innerHTML = `R$ ${valorVeiculo1.toFixed(2).replace(".", ',')}`
        displayTimeValue2.innerHTML = `R$ ${valorVeiculo2.toFixed(2).replace(".", ',')}`
    }
    activeVehicleCorrectColor(botao)
}


function deactivateVehiclesButtons() { 
    clearImgColor()
    resetColor()
    chosenCar = ''
    btnEstacionar.disabled = true
    for (let vehicle of allVehicles) {
        vehicle.classList.remove('btn-active')
        valorVeiculo1 = 0
        valorVeiculo2 = 0
        tipoVeiculo = '' 
        displayTimeValue1.innerHTML = `R$ ${valorVeiculo1.toFixed(2).replace(".", ',')}`
        displayTimeValue2.innerHTML = `R$ ${valorVeiculo2.toFixed(2).replace(".", ',')}`
    }
    totalTempo = 0
    totalValue = 0
    displayTempo.innerHTML = `${totalTempo}min`
    displayValue.innerHTML = `R$ ${totalValue.toFixed(2).replace(".", ',')}`
}


function selectVehicleType(btnClicked, filter) {
    deactivateVehiclesButtons()
    for (let button of vehicleTypeButtons) {
        button.classList.remove('btn-active')
    }
    btnClicked.classList.add('btn-active')
    for (let vehicle of allVehicles) {
        vehicle.style.display = 'none'
    }
    switch (filter) {
        case 'C':
            for (let car of cars) {
                car.style.display = 'inline-block'
            }
            break
        case 'M':
            for (let moto of motos) {
                moto.style.display = 'inline-block'
            }
            break
        case 'O':
            for (let other of others) {
                other.style.display = 'inline-block'
            }
            break
        case 'all':
            for (let vehicle of allVehicles) {
                vehicle.style.display = 'inline-block'
            }
            break
    }
    activeTypeCorrectColor(filter)
}


function statusBtnEstacionar() {
    if (totalTempo > 0 && chosenCar != '') {btnEstacionar.disabled = false}
    else {btnEstacionar.disabled = true}
}


function aumentarTempo(valorTempo, valorReais){
    checkVehicle()
    if (tipoVeiculo != '') {
        totalTempo += valorTempo
        if (valorReais == 'Tarifa Menor') {totalValue += valorVeiculo1}
        else if (valorReais == 'Tarifa Maior') {totalValue += valorVeiculo2}
        displayTempo.innerHTML = `${totalTempo}min`
        displayValue.innerHTML = `R$ ${totalValue.toFixed(2).replace(".", ',')}`
        convertTime()
        statusBtnEstacionar()
    }
}


function reduzirTempo(valorTempo, valorReais){
    checkVehicle()
    if (tipoVeiculo != '') {
        totalTempo -= valorTempo
        if (totalTempo < 0) totalTempo = 0
        if (valorReais == 'Tarifa Menor') {totalValue -= valorVeiculo1}
        else if (valorReais == 'Tarifa Maior') {totalValue -= valorVeiculo2}
        if (totalValue < 0) totalValue = 0 
        displayTempo.innerHTML = `${totalTempo}min`
        displayValue.innerHTML = `R$ ${totalValue.toFixed(2).replace(".", ',')}`
        convertTime()
        statusBtnEstacionar()
    }
}


saldoCliente = parseFloat(saldoCliente)

function showMessage(msg){
    $('#msg-estacionar').html(msg)

    $("#div-msg-estacionar").fadeIn()
    setTimeout(function() {
        $("#div-msg-estacionar").fadeOut()
    }, 2000);     
}


function checkCredits() {
    if (saldoCliente >= totalValue) showModal()
    else {
        showMessage("Saldo em conta insuficiente.");
    }
}


function checkVehicle() {
    if (chosenCar == '') showMessage("Por favor selecione um veículo!")
}


/* Time Related */
var hours_increased = 0
var minutes_increased = 0

function convertTime(){
    hours_increased = Math.floor(totalTempo / 60);          
    minutes_increased = totalTempo % 60;   
}


function checkDateTime(dateTime) {
    if (dateTime < 10) dateTime = '0' + dateTime
    return dateTime
}


var newDate = new Date(); 

var year = newDate.getFullYear()
var month = checkDateTime((newDate.getMonth()+1))
var day = checkDateTime(newDate.getDate())
var today = day + '/' + month + '/' + year

var now = newDate.getHours()  + ":" + newDate.getMinutes()  + ":" + newDate.getSeconds()

var hours = 0
var minutes = 0
var seconds = 0

function countdown(){
    if (today == dayParked) {
        if (seconds == 0) {
            seconds = 59;
            minutes--;
        } else {
            seconds--;
        }
        if (minutes == -1) {
            minutes = 59;
            hours--;
        }
        if (hours > -1) {
            let displayHours = ''
            let displayMinutes = ''
            let displaySeconds = `e ${seconds} segundos`
            if (minutes < 1) displaySeconds = `${seconds} segundos`
            displayHours = checkPlurals(displayHours, hours, 'hora')
            displayMinutes = checkPlurals(displayMinutes, minutes, 'minuto')
            spanCountdown.innerHTML = displayHours + displayMinutes + displaySeconds
            setTimeout(countdown, 1000);
        } else {
            spanCountdown.innerHTML = "Tempo Expirado."     
        }
    } else {
        spanCountdown.innerHTML = "Tempo Expirado."  
    } 
}


function checkPlurals(display, value, string) {
    if (value == 1) display = `${value} ${string} `
    else if (value > 1) {
        display = `${value} ${string}s `
    }
    return display
}


var start_time, end_time

function calculateCountdown(exp_time) {
    console.log(now)
    console.log(exp_time)
    start_time = now.split(":")
    end_time = exp_time.split(":")
    hours = parseFloat(end_time[0]) - parseFloat(start_time[0])
    minutes = parseFloat(end_time[1]) - parseFloat(start_time[1])
    if (minutes < 0) {
        minutes = minutes + 60
        hours--
    }
    seconds = parseFloat(end_time[2]) - parseFloat(start_time[2])
    if (seconds < 0) {
        seconds = seconds + 60
        minutes--
    }
    countdown()
}


if (document.getElementById('expiration-span') !== null) {
    var spanCountdown = document.getElementById('span-countdown')
    var dayParked = document.getElementById('day-parked-span').innerHTML
    var expirationTime = document.getElementById('expiration-span').innerHTML
    var parkedCar = document.getElementsByClassName('btn-countdown')[0].id 
    calculateCountdown(expirationTime)
}


function getEntryTime() {
    var today2 = new Date();
    var entry = today2.getHours() + ":" + today2.getMinutes() + ":" + today2.getSeconds();
    return entry
}


function getExpirationTime() {
    var exp_h, exp_m, exp_s
    if ((chosenCar == parkedCar) && (spanCountdown.innerHTML != "Tempo Expirado.")) {
        exp_h = parseFloat(end_time[0]) + hours_increased
        exp_m = parseFloat(end_time[1]) + minutes_increased
        if (exp_m >= 60) {
            exp_h++;
            exp_m = exp_m % 60;
        }
        exp_s = end_time[2]
    } else {
        today3 = new Date();
        exp_h = (today3.getHours()+hours_increased)
        exp_m = (today3.getMinutes()+minutes_increased)
        if (exp_m >= 60) {
            exp_h++;
            exp_m = exp_m % 60;
        }
        exp_s = today3.getSeconds()  
    }
    var expiration = exp_h + ":" + exp_m + ":" + exp_s;
    return expiration
}


/* Modal */
let modal = document.getElementById('modal-full-screen')
let modalDisplayCar = document.getElementById('modal-car')
var modalDisplayTime = document.getElementById('modal-time')
var modalMsg = document.getElementsByClassName('modal-msg')[0]
var modalObs = document.getElementsByClassName('modal-obs')[0]

function showModal() {
    if ((chosenCar == parkedCar) && (spanCountdown.innerHTML != "Tempo Expirado.")) {
        modalMsg.innerHTML = 'Você gostaria de acrescentar <strong id="modal-time"></strong> ao veículo <strong id="modal-car"></strong>?'
        modalDisplayCar = document.getElementById('modal-car')
        modalDisplayTime = document.getElementById('modal-time')
        modalObs.style.display = 'none'
    } else {
        modalMsg.innerHTML = 'Você gostaria de estacionar o veículo <strong id="modal-car"></strong> por <strong id="modal-time"></strong>?'
        modalDisplayCar = document.getElementById('modal-car')
        modalDisplayTime = document.getElementById('modal-time')
        modalObs.style.display = 'block'
    }
    modalDisplayCar.innerHTML = `"${chosenCar}"`
    if (hours_increased < 1) modalDisplayTime.innerHTML = `${minutes_increased}min`
    else if (minutes_increased == 0) {
        modalDisplayTime.innerHTML = `${hours_increased}h`
    } else {
        modalDisplayTime.innerHTML = `${hours_increased}h e ${minutes_increased}min`
    }
    modal.style.display = 'block'
}


function closeModal() {
    modal.style.display = 'none'
}


$(document).on('submit', '#estacionar_form', function() {
    let entryTime = getEntryTime()
    let expirationTime = getExpirationTime()

    $.ajax({
        type: 'POST',
        url: '',
        data: {
            license_plate: chosenCar,
            value: totalValue,
            entry_time: entryTime,
            expiration_time: expirationTime,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            
        }
    });
});
