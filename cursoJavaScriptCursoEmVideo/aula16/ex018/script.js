let recebeNumero = document.querySelector("input#txtnumero")
let resultado = document.getElementById("lista")
let res = document.getElementById("res")
let numeros = []


function isNumero(n){
    if (Number(n) >= 1 && Number(n) <= 100){
        return true
    } else {
        return false
    }
}


function inLista(n, l){
    if (l.indexOf(Number(n)) != -1){
        return true
    } else {
        return false
    }
}


function adicionar(){
    if(isNumero(recebeNumero.value) && !inLista(recebeNumero.value, numeros)){
        numeros.push(Number(recebeNumero.value))
        var adicionarItem = document.createElement(`option`)
        adicionarItem.text = `Valor ${recebeNumero.value} adicionado.`
        adicionarItem.setAttribute ('id', `i${numeros.length}`)
        adicionarItem.value = `numero${numeros.length}`
        resultado.appendChild(adicionarItem)
        res.innerHTML = ``
    } else {
        window.alert('[ERRO]: Valor inválido ou já encontrado na lista!')
    }
        recebeNumero.value = ``
        recebeNumero.focus()
}

function finalizar(){
    if (numeros.length == 0){
        window.alert(`[ERRO]: Adicione valores antes de finalizar!`)
    } else {
        var total = numeros.length
        var maior = numeros[0]
        var menor = numeros[0]
        var somaTotal = 0
        res.innerHTML = ``
        for (c = 0; c < total; c++){
            somaTotal += numeros[c]
            //SELEÇÃO DO MAIOR NÚMERO
            if (numeros[c] > maior){
                maior = numeros[c]
            }
            //SELEÇÃO DO MENOR NÚMERO
            if (numeros[c] < menor){
                menor = numeros[c]
            }
        }
        var media = somaTotal / total
        res.innerHTML += `<p>Ao todo, temos ${numeros.length} números cadastrados!</p>`
        res.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`
        res.innerHTML += `<p>Somando todos os valores temos ${somaTotal}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${media}.</p>`
    }
}