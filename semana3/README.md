# Semana 3

## Análise Exploratória de Dados

* Extremamente importante para o andamento de qualquer projeto de dados;
    * Deve ser um processo multidisciplinar(negócio, gerentes de projeto, cientistas de dados e etc.);
* **Análise Exploratória**
    * *Procedimentos para analisar dados, técnicas para interpretar resultados de tais procedimentos, formas de planejar a reunião dos dados para tornar a sua análise mais fácil, mais precisa ou mais exata e toda a maquinária e os resultados de estatística(matemática) que se aplicam a análise de dados*
    * Sugerir Hipóteses;
    * Testar e avaliar as hipóteses sugeridas;
    * Apoiar a seleção das ferramentas técnicas;
    * Oferecer uma base para coleta de dados;
* Atacar sempre o problema com a técnica mais simples primeiro e caso não seja possível aumentar a complexidade;

## Estatística Univariada

* Analisar uma variável separadamente;
* Conceitos básicos
    * Média;
        * Medidas Centrais;
        * Soma dos elementos do conjunto dividido pelo total de elementos;
        * Bastante afetado por outliers;
    * Mediana;
        * Medidas Centrais
        * É o elemento central do conjunto
        * Quanto mais distante a média está da mediana é sinal de outliers
    * Moda;
        * É o valor que mais aparece no conjunto de dados;
    * Desvio Padrão;
        * Medida de dispersão
            * O quanto os dados variam entre sí
        * Quanto mais próximo de 0 mais concentrados estão os dados   
    * Quartis
        * Muito importante na feature engeneering;
        * Muito útil para criar novas categorias ou transformar categorias existentes;
        * Amplitude Interquartil
            * É a diferença entre Q3 e Q1
            * Representado pelo Boxplot;
    * Percentis;
    * Skewness(Assimetria)
        * É o grau de distribuição da curva simétrica a distribuição normal, ou seja, pra onde ela varia - esquerda ou direita;
        * Legal pra ver pra onde estão pendendo os dados;
        * É influenciado pela moda;
    * Curtosis
        * É a medida de dispersão que trata do grau de achatamento da curva;
        * Tipos de Curtosis:
            * **Mesocurticas(0)**: 
                * Achatamento da distribuição noral
            * **Leptocúrticas(> 0)** 
                * Possui curva da função de distribuição normal mais afunilada
                * Pico mais alto do que a distribuição normal
                * Possui caudas pesadas;
            * **Platicúrtica**
                * Função de distribuição é mais achatada que a distribuição normal;
    * Padronizar as variáveis irá resultar em uma média igual a 0 r um desvio padrão igual a 1;
    * Normalizar as veriáveis significa colocá-las dentro de um intervalo de que pode variar de -1 até 1, caso haja valores negativos, e 0 até 1 caso não haja.

## Análise Exploratória
* Sempre checar primeiro a integridade dos dados, se os tipos estão corretos, e etc.;
* Quando fazemos uma análise exploratória sempre buscamos:
    * Perguntas
        * É sempre legal pensar em dados que a gente não tem dentro base;
            * Quais outras informações públicas, ou que eu posso conseguir, que me ajudariam a resolver o problema?
        * É importante analisar bem o contexto das perguntas quando formulamos as hipóteses!r
    * Hipóteses
        *São a parte mais difícil de se modelar!
## Análise Multivariada de Dados
* Correlação: medida padronizada entre a relação das duas variáveis;
    * Indica força e direção dos relacionamentos entre duas variáveis;
    * Gráfico de dispersão;
    * **Correlação não é causalidade!**
        * Correlação Expúria: **Existe correlação mas ninguém consegue explicar porque!**;
    * Correlação de Spearman:
        * **Relação monotônica entre as variáveis**;
        * **Mudar juntas mas não necessariamente a uma taxa constante**;
    * Correlação de Pearson
        * Mede uma relação linear entre duas variáveis contínuas
            * A mudança de uma variável é associada a uma mudança proporcional na outra variável
    * Uma Correlação pode variar de -1 até 1;
    * Correlação prórima de 0 indica nenhuma relção entre as veriáveis
    * Correlação positiva: Variáveis se movem juntas(na mesma direção)
        * Quanto mais próximo de 1 mais forte essa correlação
    * Correlação Negativa: Variáveis se movem juntas mas em direções opostas
        * Quanto mais próximo de -1 mais correlacionadas estão as variáveis;
    * Duas variáveis são perfeitamente correlacionadas positivamente/negativamente r=1/r=-1 movem-se em perfeita proporção na mesma direção/direções opostas

## Visualização de Dados

* É imprescindível para a ciência de dados!
    * **Permite ao cientista de dados apresentar os seus resultados de forma mais amigável!**
* Deve-se levar em conta o tipo de indivíduo que vai ler o que estamos produzindo!
* Exemplos:
    * Histograma:
        * Utilizado pra visualizar distribuições de frequência;
    * Box Plot
        * Conseguimos Visualizar mediana, min, max, primeiro quartil, segundo quartil, terceiro quartil, IQR e outliers;
    * Scatter plot
        * Gráfico de dispersão
            * É exibido como uma coleção de pontos onde cada ponto representa uma observação da nossa base
    * Matriz de Correlação ou Heat Map


        
    

