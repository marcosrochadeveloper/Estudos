function parOuImpar(n){
    if (n%2 == 0){
        return 'Par'
    } else{
        return 'Ímpar'
    }
}

for (c=1; c<=10;c++){
console.log(`O número ${c} é ${parOuImpar(c)}`)
}