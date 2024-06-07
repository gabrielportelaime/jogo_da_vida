Não entendo como um algoritmo tão simples pode gerar esses resultados. 

Consiste num tabuleiro "infinito" em que cada posição pode estar "viva" ou "morta". 
Cada posição no tabuleiro possui 8 posições vizinhas que também podem estar "vivas" ou "mortas" cada uma.

Regras (Ao se percorrer o tabuleiro):

1) Se a posição está "viva" e está cercada por posições "mortas" então ela MORRE de solidão;
2) Se a posição está "viva" e possui 4 ou mais posições "vivas" nos seus arredores, ela morre por supermutação;
3) Se a posição está "morta" e possui 3 posições "vivas" nos seus arredores, ela NASCE.

<h1>Vídeo de funcionamento do algoritmo em Python.</h1>

![simulacao py - jogo_da_vida - Visual Studio Code 2024-06-07 13-13-21](https://github.com/gabrielportelaime/jogo_da_vida/assets/90880142/162fa6bd-a271-4f1b-8f6b-2bda03678cba)

<h1>Imagem inicial do tabuleiro (100x100)</h1>

![inicio](https://github.com/gabrielportelaime/jogo_da_vida/assets/90880142/382daec2-010d-41ba-a49c-2aafd703874f)

<h1>Imagem final do tabuleiro (100x100)</h1>

![fim](https://github.com/gabrielportelaime/jogo_da_vida/assets/90880142/de73e5c1-62e9-4879-910c-f4d67dfe3e77)

