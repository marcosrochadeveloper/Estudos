var idade = 12
console.log(`Você tem ${idade} anos`)
if (idade < 16) {
    console.log(`E ainda não pode votar!`)
} else if (idade < 18 || idade >= 65){
        console.log(`E a votação para você é opcional!`)
    } else {
        console.log(`E tem a obrigação de votar!`)
    }