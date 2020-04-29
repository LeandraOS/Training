let $altura =document.querySelector('#altura');
let $peso = document.querySelector('#peso');
// parametro do query selector é para que
// quando vc coloca a gradinha isso quer dizer que é pra procurar algo que tenha o id 
//imc
let $button = document.querySelector('button');
function update(){
    let altura = Number($altura.value);
    let peso = Number($peso.value);
    let imc = peso/ (altura * altura);
    let elementos = document.querySelectorAll('.imc');

    for(let i= 0; i < elementos.length; i++){
        elementos[i].innerText = imc;
    }
}

$button.addEventListener('click', update);
//estilizacao css
//estruturacao html
//logica js
//os tres se reunem no DOM