let nome = "Matheus"

function saudacao(){
    console.log(`Olá, ${nome}!`);
}
saudacao()


function apresentacao(){
    let sobrenome = "Duarte"
    console.log(`Olá, ${sobrenome}!`);
    
}

apresentacao()
//console.log(sobrenome); erro


//closure

function apresentandoAlguem(){
    let nome = "Matheus Duarte"
    function saudacao(){
        console.log(`Olá, ${nome}`);
    }
    function despedida(){
        console.log(`Até mais, ${nome}`);
    }
    return{
        saudacao1: saudacao,
        despedida: despedida
    }
}

const pessoa = apresentandoAlguem()

pessoa.saudacao1()
pessoa.despedida()