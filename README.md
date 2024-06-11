# Tecnosolo Sondagem - Permeabilidade do Solo
#Desenvolvido por: Lucas Zozo

Tecnosolo Sondagem, uma ferramenta interativa para calcular a permeabilidade do solo. Este programa utiliza o método de percolação para determinar a permeabilidade com base em dados fornecidos pelo usuário. A aplicação foi desenvolvida utilizando a biblioteca Tkinter do Python, proporcionando uma interface gráfica amigável e intuitiva.

## Funcionalidades

- **Entrada de dados**: Insira a altura inicial e final da coluna de solo.
- **Seleção do tipo de solo**: Escolha entre vários tipos de solo, como areia fina, areia média, areia grossa, areia siltosa, siltes e argilas.
- **Cálculo de permeabilidade**: O programa calcula a permeabilidade do solo em cm/s e m/s.
- **Resultados detalhados**: Veja uma janela com os resultados detalhados, incluindo o tipo de solo, a faixa de permeabilidade esperada, o volume de água percolado e a permeabilidade calculada.

## Como usar

1. **Execute o programa**: Inicie o programa executando o script Python.
2. **Insira os dados**:
    - **Altura inicial (cm)**: A altura inicial da coluna de solo.
    - **Altura final (cm)**: A altura final da coluna de solo após a percolação.
    - **Tipo de solo**: Selecione o tipo de solo da lista suspensa.
3. **Calcular**: Clique no botão "Calcular" para obter os resultados.

## Exemplo de uso

1. Insira a altura inicial da coluna de solo (ex.: 100 cm).
2. Insira a altura final da coluna de solo (ex.: 80 cm).
3. Selecione "Areia média" como o tipo de solo.
4. Clique em "Calcular".
5. Uma nova janela aparecerá mostrando os resultados, como o volume de água percolado e a permeabilidade do solo.

## Instalação

Para executar este programa, você precisa ter o Python instalado em seu computador. Se não tiver o Tkinter instalado, você pode instalá-lo utilizando o seguinte comando:

```bash
pip install tk
