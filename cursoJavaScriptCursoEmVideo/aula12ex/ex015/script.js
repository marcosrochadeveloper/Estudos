function verificar(){
    //Declaração de Variáveis
    var data = new Date()
    var anoAtual = data.getFullYear()
    var anoNascimento = window.document.getElementById('txtano')
    var res = window.document.querySelector('div#res')
    if (Number(anoNascimento.value.length) == 0 || Number(anoNascimento.value) > anoAtual) {
        window.alert(`[ERRO]: Verifique os dados e tente novamente!`)
    } else {
        var sexo = document.getElementsByName('radsex')
        var idade = anoAtual - Number(anoNascimento.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (sexo[0].checked) {
            genero = 'um Homem'
            if (idade < 10) {
                img.setAttribute('src', 'foto-bebe-m.png')
            } else if (idade < 21){
                img.setAttribute('src', 'foto-jovem-m.png')
            } else if (idade < 50){
                img.setAttribute('src', 'foto-adulto-m.png')
            } else {
                img.setAttribute('src', 'foto-idoso-m.png')
            }


        }   else if (sexo[1].checked) {
            genero = 'uma Mulher'
            if (idade < 10) {
                img.setAttribute('src', 'foto-bebe-f.png' )
            } else if (idade < 21) {
                img.setAttribute('src', 'foto-jovem-f.png')
            } else if (idade < 50){
                img.setAttribute('src', 'foto-adulto-f.png')
            } else {
                img.setAttribute('src', 'foto-idoso-f.png')
            }

        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos de idade!`
        res.appendChild(img)
    }
}