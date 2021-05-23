# Editor de imagens
Este programa permite a edição de imagens através a aplicação de alguns filtros e a transformação geométrica.

## Como foi desenvolvido?
O programa foi desenvolvido utilizando a biblioteca Opencv para manipulação das imagens e PySimpleGui para a montagem da tela. Também foram desenvolvidos métodos próprios para aplicação de filtros no domínio da frequência. O programa está utilizando o modelo de classes.

## Filtros disponíveis
### Filtros espaciais
- Blur (Borramento)
- Blur Gaussiano (Borramento)
- Blur Mediana
- Sobel X
- Sobel Y
- Laplaciano
- Canny

### Filtros no domínio da frequência
- Passa alta
- Passa baixa

### Transformações geométricas
- Escala
- Ângulo
- Espelhamento
- Translação

## Como iniciar o programa?
Execute o arquivo main.py pelo terminal, utilizando o comando `python3 main.py`.