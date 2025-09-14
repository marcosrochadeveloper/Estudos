function calcular(){
    let resultado = document.getElementByid = "resultado";
    let nome = document.getElementByid = "txtnome";
    let altura = document.getElementByid = "txtaltura";
    let peso = document.getElementByid = "txtpeso";
    let imc = peso / (altura*altura);

    resultado.innerHTML = `${nome} seu IMC é ${imc} e você`;
    

}