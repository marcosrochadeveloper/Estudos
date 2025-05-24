function contagem(){
let inicio = window.document.getElementById('txti')
let fim = window.document.getElementById('txtf')
let passo = window.document.getElementById('txtp')
let res = window.document.getElementById('res')
res.innerHTML = ''

    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        res.innerHTML= 'Impossível Contar!'
    //SE O PASSO FOR 0
    } else{
        var i = Number(inicio.value)
        var f = Number(fim.value)
        var p = Number(passo.value)
        res.innerHTML = `Contando...<br>`
        if (p == 0){
            alert('[ERRO]: Passo inválido, considerando PASSO 1!!!');
            p = 1
        }
        if (i < f){
            //CONTAGEM CRESCENTE
            for (c = i; c <= f; c += p){
                res.innerHTML += `${c}\u{1F449} `;
            }
        } else {
            //CONTAGEM REGRESSIVA
            for (c = i; c >= f; c -= p){
                res.innerHTML += `${c}\u{1F449} `;
            }
        }
                       res.innerHTML += `\u{1F3F4}`
    }
}