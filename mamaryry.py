class Exercicios:
    def calcular_expressoes(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5
        
        # Calculando e mostrando cada caso
        print("Valor1 + Valor2:", valor1 + valor2)
        print("Valor1 + Valor2 + Valor4:", valor1 + valor2 + valor4)
        print("Valor1 + Valor2 - Valor5:", valor1 + valor2 - valor5)
        print("Valor1 + Valor3 (concatenação):", str(valor1) + valor3)
        print("Valor1 * Valor2:", valor1 * valor2)
        print("(Valor4 * Valor2) / 2:", (valor4 * valor2) / 2)
        print("(Valor1 + Valor2 + Valor4 + Valor5) / 4:", (valor1 + valor2 + valor4 + valor5) / 4)

# Chamada do método para calcular as expressões
ex = Exercicios()
ex.calcular_expressoes()
class Exercicios:
    def calcular_soma_media(self):
        v1 = 2
        v2 = 3
        v3 = 5
        v4 = 6
        
        # Calculando a soma dos valores
        soma = v1 + v2 + v3 + v4
        
        # Calculando a média dos valores
        media = soma / 4
        
        # Mostrando os resultados
        print("Soma dos valores:", soma)
        print("Média dos valores:", media)

# Chamada do método para calcular a soma e a média
ex = Exercicios()
ex.calcular_soma_media()
class Exercicios:
    def verificar_aprovacao(self):
        nota1 = 64
        nota2 = 45
        nota3 = 60
        
        # Calculando a média das notas
        media = (nota1 + nota2 + nota3) / 3
        
        # Verificando se o aluno está reprovado ou aprovado
        if media >= 60:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado.")

# Chamada do método para verificar a aprovação
ex = Exercicios()
ex.verificar_aprovacao()
class Exercicios:
    def verificar_aprovacao(self):
        nota1 = 64
        nota2 = 45
        nota3 = 60
        
        # Calculando a média das notas
        media = (nota1 + nota2 + nota3) / 3
        
        # Verificando se o aluno está aprovado com certificado, apenas aprovado ou reprovado
        if media >= 90:
            print("O aluno foi aprovado com certificado!")
        elif media >= 60:
            print("O aluno está aprovado!")
        else:
            print("O aluno está reprovado.")

# Chamada do método para verificar a aprovação
ex = Exercicios()
ex.verificar_aprovacao()
function exercicio1() {
  // Variáveis para armazenar informações do funcionário
  var nomeFuncionario = "João Silva";
  var idadeFuncionario = 30;
  var salarioFuncionario = 3000.00;
  var cargoFuncionario = "Analista de Dados";
  var turnoFuncionario = "Matutino";
  var setorFuncionario = "TI";

  // Exibindo informações do funcionário
  console.log("Informações do Funcionário:");
  console.log("Nome:", nomeFuncionario);
  console.log("Idade:", idadeFuncionario);
  console.log("Salário:", salarioFuncionario);
  console.log("Cargo:", cargoFuncionario);
  console.log("Turno:", turnoFuncionario);
  console.log("Setor:", setorFuncionario);
}

// Chamada da função
exercicio1();
function exercicio2() {
  // Variáveis para armazenar informações da escola
  var nomeEscola = "Escola Estadual ABC";
  var estado = "São Paulo";
  var numProfessores = 50;
  var cidade = "São Paulo";
  var numMilitares = 10;
  var logradouro = "Rua das Escolas, 123";
  var numero = "Centro";
  var numAlunos = 1000;
  var disciplinas = ["Matemática", "Português", "Ciências", "História"];

  // Exibindo informações da escola
  console.log("Informações da Escola:");
  console.log("Nome da Escola:", nomeEscola);
  console.log("Estado:", estado);
  console.log("Número de Professores:", numProfessores);
  console.log("Cidade:", cidade);
  console.log("Número de Militares:", numMilitares);
  console.log("Logradouro:", logradouro);
  console.log("Número:", numero);
  console.log("Número de Alunos:", numAlunos);
  console.log("Disciplinas:", disciplinas.join(", "));
}

// Chamada da função
exercicio2();
function exercicio3() {
  // Dados
  var valor1 = 10;
  var valor2 = 5;
  var valor3 = "2"; // Será convertido para número ao ser usado em operações matemáticas
  var valor4 = 8;
  var valor5 = -5;

  // Calculando e mostrando cada caso
  console.log("valor1 + valor2:", valor1 + valor2);
  console.log("valor1 + valor2 + valor4:", valor1 + valor2 + valor4);
  console.log("valor1 + valor2 - valor5:", valor1 + valor2 - valor5);
  console.log("valor1 + valor3:", valor1 + Number(valor3)); // Convertendo valor3 para número
  console.log("valor1 * valor2:", valor1 * valor2);
  console.log("(valor4 * valor2) / 2:", (valor4 * valor2) / 2);
  console.log("(valor1 + valor2 + valor4 + valor5) / 4:", (valor1 + valor2 + valor4 + valor5) / 4);
}

// Chamada da função
exercicio3();
function exercicio4() {
  // Dados
  var v1 = 2;
  var v2 = 3;
  var v3 = 5;
  var v4 = 6;
  
  // Calculando a soma dos valores
  var soma = v1 + v2 + v3 + v4;
  
  // Calculando a média dos valores
  var media = soma / 4;
  
  // Mostrando os resultados
  console.log("Soma dos valores:", soma);
  console.log("Média dos valores:", media);
}

// Chamada da função
exercicio4();
function exercicio5() {
  // Dados
  var nota1 = 64;
  var nota2 = 45;
  var nota3 = 60;

  // Calculando a média das notas
  var media = (nota1 + nota2 + nota3) / 3;

  // Verificando se o aluno está reprovado ou aprovado
  if (media >= 60) {
    console.log("O aluno está aprovado!");
  } else {
    console.log("O aluno está reprovado.");
  }
}

// Chamada da função
exercicio5();
function exercicio6() {
  // Dados
  var nota1 = 70;
  var nota2 = 85;
  var nota3 = 90;

  // Calculando a média das notas
  var media = (nota1 + nota2 + nota3) / 3;

  // Verificando se o aluno foi aprovado com certificado, apenas aprovado ou reprovado
  if (media >= 90) {
    console.log("Aluno foi aprovado com certificado!");
  } else if (media >= 60) {
    console.log("Aluno está apenas aprovado.");
  } else {
    console.log("Aluno está reprovado.");
  }
}

// Chamada da função
exercicio6();
function exercicio6() {
  // Dados
  var nota1 = 70;
  var nota2 = 85;
  var nota3 = 90;

  // Calculando a média das notas
  var media = (nota1 + nota2 + nota3) / 3;

  // Verificando se o aluno foi aprovado com certificado, apenas aprovado ou reprovado
  if (media >= 90) {
    console.log("Aluno foi aprovado com certificado!");
  } else if (media >= 60) {
    console.log("Aluno está apenas aprovado.");
  } else {
    console.log("Aluno está reprovado.");
  }
}

// Chamada da função
exercicio6();
