let valores = [8,1,7]
valores.push(4,2,9,6)
valores.sort()
console.log(`Nosso vetor tem as numerações ${valores} totalizando ${valores.length} posições`)

/*for (let contador = 0; contador < valores.length; contador++) {
    console.log(`A posição ${contador} do vetor tem o valor ${valores[contador]}`)
}*/

for (let contador in valores ) {
    console.log(`A posição ${contador} do vetor tem o valor ${valores[contador]}`)
}

pos3 = valores.indexOf(3)

pos8 = valores.indexOf(8)

if (pos3 == -1){
    console.log(`[ERRO]: Valor 3 não encontrado!`)
} else {
    console.log(`O valor 3 está na posição ${pos3}`)
}

if (pos8 == -1){
    console.log(`[ERRO]: Valor 8 não encontrado!`)
} else {
    console.log(`O valor 8 está na posição ${pos8}`)
}