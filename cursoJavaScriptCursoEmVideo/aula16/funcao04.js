function fatorial(n){
    let fat = 1
    for (n; n > 1; n--){
        fat *= n
        console.log(`${fat}x${n-1} = ${fat*(n-1)}`)
    }
    return fat
}

fato = 5
console.log(`o fatorial de ${fato} é igual a ${fatorial(fato)}`)