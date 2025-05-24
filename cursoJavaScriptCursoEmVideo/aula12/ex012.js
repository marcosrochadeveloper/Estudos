var agora = new Date()
var diasemana = agora.getDay()
switch (diasemana) {
    case 0:
        diasemana = "Domingo"
        break
    case 1:
        diasemana = "Segunda-feira"
        break
    case 2:
        diasemana = "Terça-Feira"
        break
    case 3:
        diasemana = "Quarta-Feira"
        break
    case 4:
        diasemana = "Quinta-Feira"
        break
    case 5:
        diasemana = "Sexta-Feira"
        break
    case 6:
        diasemana = "Sábado"
        break
    default:
        diasemana = "[ERRO]: Dia Inválido, contate um profissional de TI."
}

var hora = agora.getHours()
var minutos = agora.getMinutes()
var segundos = agora.getSeconds()
var horacompleta = `${hora}:` + `${minutos}:` + `${segundos}`
console.log(`Hoje é ${diasemana}.`)
console.log(`Agora são exatamente ${horacompleta}.`)
if (hora < 6 ) {
    console.log(`Boa Madrugada`)
} else if (hora < 12){
    console.log(`Bom Dia`)
} else if (hora < 18){
    console.log(`Boa Tarde`)
} else if (hora < 24){
    console.log(`Boa Noite`)
} else if (hora >= 24) {
    console.log(`Hora Inválida`)
}