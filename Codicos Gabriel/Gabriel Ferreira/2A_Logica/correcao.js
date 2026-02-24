//Exer 1 e Exer 2
var dados = {
  nome: 'Murilo ',
  sobrenome: 'Ribeiro',
  nomeCompleto(){
    return (`Meu nome é ${this.nome + this.sobrenome}`)
  }
}

console.log(dados.nomeCompleto())

//Exer 3
var carro = {
  preco: 1000,
  portas: 4,
  marca: 'Audi',
}
carro.preco = 3000;

//Exer 4
var cachorro = {
  raca: 'Labrador',
  cor: 'preto',
  idade: 10,
  verHomem: true,
  latir(){
    if(this.verHomem){
    return ('Au Au Au')
  }}
}
console.log(cachorro.latir())

nome = 'Murilo'
console.log(nome.charAt(1));

var altura = 0.5;

altura.toString(); // '1.8'
console.log(altura.toFixed()); // '2'

function areaQuadrado(lado) {
  return lado * lado;
}

console.log(areaQuadrado.toString());
//"function areaQuadrado(lado) {
//  return lado * lado;
//}"
