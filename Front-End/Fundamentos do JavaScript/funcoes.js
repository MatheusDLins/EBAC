function descobrirIdade(anoNascimento){
    return 2024 - anoNascimento
}

console.log(descobrirIdade(2001));

function somarNumeros( numA, numB, numC){
    return numA + numB + numC
}

console.log(somarNumeros(10, 20, 30));


function somarNumeros( numA, numB, numC){
    let resultado = numA + numB + numC
    return console.log('O resultado foi: ' + resultado);
    
}

somarNumeros(30, 30, 30)