# Projeto: Calculadora de IMC

## Descrição

Este projeto implementa uma calculadora de Índice de Massa Corporal (IMC), que permite ao usuário inserir seus dados de peso e altura para calcular o IMC e identificar a categoria de peso, como abaixo do peso, peso normal, sobrepeso ou obesidade.

## Alunos

- **Pedro Hugo Coura** (GES - 245)
- **Lucas Sawada Obana** (GES - 241)

## Funcionalidades

- Entrada de peso (kg) e altura (m).
- Cálculo automático do IMC.
- Exibição da categoria de IMC com base no valor calculado:
  - Abaixo do peso
  - Peso normal
  - Sobrepeso
  - Obesidade

## Objetivo

O objetivo do projeto é criar uma ferramenta simples e acessível para calcular o IMC, promovendo conscientização sobre saúde e bem-estar através da interpretação fácil dos resultados.

## Como usar

1. **Instalar as dependências do Playwright**

   Execute o seguinte comando no terminal para instalar o pacote `pytest-playwright`:

   ```bash
   pip install pytest-playwright
   ```

2. **Após instalar as dependências**

   Você pode rodar os testes utilizando o Pytest. Para isso, execute o comando:`pytest test_imc.py`:

   ```bash
   pytest test_imc.py
   ```

3. **Extra**

    Para gerar um report em html do teste você deve primeiro baixar as dependências com o comando: `pip install pytest-html`:

    ```bash
    pip install pytest-html
    ```
    Por fim, rode o comando: `pytest --html=report.html`
    ```bash
    pytest --html=report.html
    ```
