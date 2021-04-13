var value;
function botao(num){
valor = document.calc.visor.value += num;
}
function reseta(){
    document.calc.visor.value = '';

}
function calcula(){
    resul = eval(valor);
    document.calc.visor.value = resul.toLocaleString('pt - br');

}