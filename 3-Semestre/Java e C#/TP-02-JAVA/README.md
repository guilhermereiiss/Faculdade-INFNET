# ![Java Logo](https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg)

#  Exercícios de Programação em Java

##  Parte 1. Escrever programas que utilizam entrada do usuário

###  Exercício 1: Cadastro de Usuário Completo
**Enunciado**

Crie um programa em Java que solicite ao usuário seu nome completo, idade, nome da mãe e nome do pai. O programa deve exibir as informações de forma organizada e verificar se o nome do usuário tem mais letras que o nome da mãe ou do pai.

**Observações:**

- Utilize a classe Scanner para capturar todas as entradas do usuário.
- Compare os tamanhos das strings para determinar o nome mais longo.

**Considerações:**

- Uso correto da classe Scanner para entrada de dados.
- Comparação correta do tamanho das strings.
- Exibição organizada das informações.

###  Exercício 2: Calculadora de Média de Notas
**Enunciado**

Desenvolva um programa que solicite ao usuário quatro notas bimestrais. O programa deve calcular a média e informar se o usuário foi aprovado (média >= 7), está em recuperação (média entre 5 e 6.9) ou foi reprovado (média < 5).

**Observações:**

- Utilize a classe Scanner para entrada de dados.
- Realize o cálculo da média aritmética.
- Exiba uma mensagem personalizada com o resultado.

**Considerações:**

- Uso correto da classe Scanner.
- Cálculo correto da média.
- Verificação correta das condições para aprovação, recuperação e reprovação.

###  Exercício 3: Conversor de Moedas
**Enunciado**

Crie um programa que peça ao usuário um valor em reais e uma moeda de destino (dólar, euro ou libra). O programa deve converter o valor informado na moeda escolhida com base em taxas de câmbio pré-definidas no código.

**Observações:**

- Utilize a classe Scanner para capturar o valor e a moeda de destino.
- Defina as taxas de câmbio diretamente no código.
- Exiba o valor convertido com duas casas decimais.

**Considerações:**

- Uso correto da classe Scanner para entrada de dados.
- Conversão correta do valor com base na taxa de câmbio.
- Formatação adequada da saída com duas casas decimais.

###  Exercício 4: Calculadora de Idade em Dias
**Enunciado**

Escreva um programa que solicite a data de nascimento do usuário (dia, mês e ano) e calcule sua idade em dias.

**Observações:**

- Utilize a classe Scanner para capturar a data de nascimento.
- Considere anos bissextos no cálculo.
- Exiba a idade total em dias.

**Considerações:**

- Uso correto da classe Scanner para entrada de dados.
- Cálculo correto considerando anos bissextos.
- Exibição correta do total de dias.

## Parte 2. Escrever códigos usando elementos de controle de fluxo

###  Exercício 5: Calculadora de Descontos Progressivos

Crie um programa que solicite o valor de uma compra e calcule o desconto aplicável com base no valor total. Se o valor for maior que R$ 1000, aplique um desconto de 10%; entre R$ 500 e R$ 1000, aplique 5%; abaixo de R$ 500, não há desconto.

**Observações:**

- Utilize estruturas condicionais para verificar o valor e aplicar o desconto.
- Exiba o valor original, o desconto aplicado e o valor final.

**Considerações:**

- Uso correto das estruturas condicionais.
- Cálculo correto do desconto e do valor final.
- Exibição clara das informações.

###  Exercício 6: Verificador de Ano Bissexto
**Enunciado**

Desenvolva um programa que peça um ano ao usuário e verifique se ele é bissexto.

**Observações:**

- Utilize estruturas condicionais para verificar as condições de ano bissexto.
- Exiba uma mensagem indicando se o ano é ou não bissexto.

**Considerações:**

- Uso correto das estruturas condicionais.
- Lógica correta para verificação de ano bissexto.
- Exibição clara da mensagem final.

###  Exercício 7: Calculadora de Imposto de Renda

Crie um programa que solicite ao usuário seu salário bruto anual e calcule o imposto de renda a pagar com base em alíquotas definidas no código. Utilize faixas de renda progressivas para calcular o imposto.

**Observações:**

- Utilize estruturas condicionais para aplicar as alíquotas.
- Exiba o valor do imposto a pagar e o salário líquido.

**Considerações:**

- Uso correto das estruturas condicionais.
- Cálculo correto do imposto de renda progressivo.
- Exibição organizada das informações.

###  Exercício 8: Classificação de Triângulos

Escreva um programa que solicite ao usuário os comprimentos de três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno.

**Observações:**

- Utilize estruturas condicionais para verificar os tipos de triângulo.
- Verifique também se as medidas formam um triângulo válido.

**Considerações:**

- Uso correto das estruturas condicionais.
- Verificação correta da validade do triângulo.
- Classificação correta do tipo de triângulo.

##  Parte 3. Escrever códigos usando instruções de repetição

###  Exercício 9: Validador de Senha
**Enunciado**

Crie um programa que solicite ao usuário que cadastre uma senha e, em seguida, peça a senha novamente até que seja digitada corretamente.

**Observações:**

- Utilize um laço de repetição para solicitar a senha até que esteja correta.
- Exiba uma mensagem de sucesso ao final.

**Considerações:**

- Uso correto do laço de repetição.
- Comparação correta das strings para validar a senha.
- Exibição correta da mensagem de sucesso.

###  Exercício 10: Jogo de Adivinhação
**Enunciado**

Desenvolva um jogo de adivinhação em que o usuário deve descobrir um número gerado aleatoriamente pelo programa (entre 1 e 100). O programa deve informar se o palpite é maior ou menor que o número sorteado até que o usuário acerte.

**Observações:**

- Utilize um laço de repetição para permitir múltiplos palpites.
- Utilize a classe Random para gerar o número secreto.

**Considerações:**

- Uso correto do laço de repetição.
- Comparação correta do palpite com o número secreto.
- Exibição adequada das dicas para o usuário.

