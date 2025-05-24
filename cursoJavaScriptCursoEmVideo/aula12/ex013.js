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

console.log(`Hoje é ${diasemana}`)