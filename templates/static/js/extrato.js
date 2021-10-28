let startDate = document.getElementById('id_date_range_0')
let endDate = document.getElementById('id_date_range_1')
let divDateRange = document.getElementById('div-date-range')

var date, year, month, day, today

function verifyMonthDay() {
    if (month < 10) month = '0'+month
    if (day < 10) day = '0'+day
}


function getDateNow() {
    date = new Date()
    year = date.getFullYear()
    month = (date.getMonth()+1)
    day = date.getDate()
    verifyMonthDay() 
    today = day+'/'+month+'/'+year
}


function setToday() {
    getDateNow()
    startDate.value = today
    endDate.value = today
}


function setLastWeek() {
    getDateNow()
    day -= 7
    if (day < 1) {
        day = day + 30
        month--
    }
    if (month < 1) {
        month = 12
        year--
    }
    verifyMonthDay()
    let lastWeek = day+'/'+month+'/'+year
    startDate.value = lastWeek
    endDate.value = today
}


function setThisMonth() {
    getDateNow()
    startDate.value = '01'+'/'+month+'/'+year
    endDate.value = today
}


function setThisYear() {
    getDateNow()
    startDate.value = '01/01/'+year
    endDate.value = today
}


$('#id_date_range_0').mask('00/00/0000', {placeholder: "dd/mm/aaaa"});
$('#id_date_range_1').mask('00/00/0000', {placeholder: "dd/mm/aaaa"});
$('#id_start_value').mask('000.00', {placeholder: "R$ 0,00", reverse: true});
$('#id_end_value').mask('000.00', {placeholder: "R$ 0,00", reverse: true});
