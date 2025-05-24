function gerarTabuada(){
    var numero = window.document.getElementById('numeroTXT').value
    //var res = window.document.getElementById('res')
    var resTabuada = window.document.getElementById('resultadoTabuada')
    var spanErros = window.document.getElementById('erros')

    if (numero.length == 0){
        alert('[ERRO]: Por favor Digite um Número!!!')
        spanErros.innerHTML = `<br><br>Não é possível gerar a Tabuada se não for informado um número!!!`
    } else {
        var numero = Number(numero)
        resTabuada.innerHTML = ``
        spanErros.innerHTML = ``
        for (c = 1; c <= 10; c++){
        var item = window.document.createElement('option')
        item.text = `${numero} x ${c} = ${numero * c}`

        //DEFINIR O ID DE CADA OPTION CRIADO
        item.setAttribute('id', `i${c}`)

        //DEFINIR O VALUE DE CADA OPTION CRIADO
        item.value = `tab${c}`

        //CRIAR UM NOVO OPTION "FILHO" DO SELECT COM ID "resultadoTabuada"
        resTabuada.appendChild(item)
        
        }
    }
}

