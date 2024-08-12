let fruta;

fruta = 'banana'

const animal = 'cachorro';

//erro
//const animal = 'girafa';

animal = 'gato'

alert(animal)

/** 
1. var
-Escopo: O escopo de var é global ou de função.
-Elevação (Hoisting): Variáveis declaradas com var são "elevadas" para o topo de seu escopo, mas não são inicializadas.
-Reatribuição: Pode ser reatribuída.


2. let
-Escopo: O escopo de let é de bloco.
-Elevação (Hoisting): let é elevado, mas não pode ser acessado antes de sua declaração (tem um comportamento chamado "temporal dead zone").
-Reatribuição: Pode ser reatribuída.


3. const
-Escopo: O escopo de const também é de bloco.
-Elevação (Hoisting): Assim como let, const é elevado, mas não pode ser acessado antes de sua declaração.
-Reatribuição: Não pode ser reatribuída. A variável é constante e seu valor não pode ser mudado.

*/