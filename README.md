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
- Primeiramente é necessário ter instalado o `python3`, `python3-tk` e `pip`
- Após, é preciso instalar as dependências com o comando `pip install -r requirements.txt`
- Com todas as dependências instaladas é possível executar o arquivo `main.py` pelo terminal, utilizando o comando `python3 main.py`