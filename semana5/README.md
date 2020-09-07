# Semana 5 - Metodologia Científica e Testes Estatísticos

## A complexidade do conhecimento
* Globalidade: Um mesmo fenômeno tem impactos e provica resultados diferentes dependendo do contexto social;
* Multidimensional: Quando realizamos uma análise devemos levar em conta que o ser humano é um aninal complexo!
* Complexo: Teroai da complexidade busca a uniãodo ser-humano e dos saberes;

**Os sete saberes necessário do futuro - Edgar Morrand**

## Pesquisa Científica
* Pesquisar: pesquisar é procurar! Pesquisar é procurar de maneira siatemática e racional por respostas aos problemas que são propostos
* Uma pesquisa é desenvolvida mediante o consurso dos conhecimentos disponíveis e a utilização cuidadodsa de métodos, técnicas e outros procedimentos científicos;
* Algumas qualidades do pesquisados:
  * Conhecimento sobre o assunto pesquisado;
  * Curiosidade;
  * Criatividade;
  * Integridade;
  * Resiliência;
  * Confiança na metodologia proposta;
* O problema científico: é uma questão não resolvida, ou resolvida de forma não adequada, e que é objeto de discussão em qualquer domínio do donhecimento;
* Para elaborar um problema científico, devemos:
    * Deve-se ter um problema metodologicamente formulado;
    * Deve-se relacionar variáveis que podem ser medidas;
    * São características do problema científico:
      * O problema deve ser formulado como pergunta;
        * É a maneira mais fácil e direta de formular um problema e deve facilitar a identificação por parte de quem consulta do que se pretende responder
        * Deve-se evitar a ambiguidade!
      * O problema deve ser claro e preciso;
        * Deve-se expressar e dimensionar as veriáveis comportadas pelo problema deixando bem claro os métodos utilizadfos para medir essas variáveis;
        * Evitar perguntas com respostas subjetivas!
      * O problema deve ser empírico;
      * O problema deve ser suscetível de solução;
        * Ao elaborar um problema deve-se ter domínio do campo e da tecnologia necessária para solucionar esse problema;
      * O problema deve ser delimitado a uma dimensão viável;
        * Problemas devem ser delimitados a dimensões viáveis:
        * Ex: O que pensam os jovens?
          * E necessário delimitar isso a uma população viável para o estudo:
            * o que os Jovens do sexo masculino de 18 a 25 anos pensam sobre compras online?

**Como elaboras projetos de pesquisa - Antônio Carlos Gil, 2002, Editora Atlas. 4ª Edição**

## Construindo Hipóteses - PARTE 1
* Se a pesquisa inicia-se com um problema, a solução prévia do problema é chamada hipótese
* Se temos uma pergunta, criamos algumas hipóteses, que são possíveis respostas para a pergunta inicial e que devem ser verificadas seguindo todo um procedimento metodológico;
  * Hipóteses Casuísticas: Hipóteses que de referem a algo que ocorre em determinado caso; Afirmam que um objeto, uma pessoa ou um fato específico tem determinada característica
    * Muito utilizada em pesquisa Histórica, onde os fatos são percebidos como únicos
  * Hipóteses de Frequencia: De modo geral, antecipam qye determinada característica ocorre com maios ou menor frequencia em determinado grupo, sociedade ou cultura;
  * Hipóteses que estabelecem relação entre variáveis: tem como objetivo conferir maior precisão aos enunciados científicos, sejam hipóteses, teorias, leis, princípios ou generalizações
  * Hipóteses que estabelecem relação de dependência entre duas ou mais variáveis: estabelece que uma variável interfere na outra, tendo por vezes, uma relação de causalidade entre elas(causalidade é diferente de correlação)

## Construindo Hipóteses - PARTE 2
* O processo de elaboração da hipótes é de natureza criativa!;
  * Observação Assistemática: O estabelecimento assistemático de relações entre os fatos do dia-a-dia é que fornece os indícios para a solução dos problemas propostos pela ciência;
  * Intuição;
  * Observação Sistemática: as observações são metódicamente orientadas;
    * Dela se extrai as características e/ou a frequência que ocorrem determinados fenômenos;
    *  *Requer estudo prévio*
  * Revisão Bibliográfica: As hipóteses realizas com base nos resultados de outras investigações geralmente conduzem a conhecimentos mais amplos que aquelas decorrentes sa cimples observação;
  * Hipóteses baseadas em teorias gerais;
* As hipóteses devem ser tão simples quanto possíveis! desde que resolvam o problema proposto;
* Devem estar relacionadas a terorias(de preferência) e devem estar alinhadas as tecnologias necessárias para o seu desenvolvimento;

**Como elaboras projetos de pesquisa - Antônio Carlos Gil, 2002, Editora Atlas. 4ª Edição**

## Contexto para Data Science
* Dosar sempre a ciência e o rigor do método científico com o negócio;
  * Um dos grandes desafios do cientista de dados é transcrever um problema de negócio para um problema científico!

## Teorema do Limite Central
* A distribuição das médias retiradas de uma amostra cuja população tenha qualquer distribuição terão uma distribuição normal;
  
## Testes Estatísticos
* Ferramenta utilizada para dizer se uma hipótese qualquer que esteja sendo experimentada tem alguma significância a nível estatístico ou não;
  * O Caminho para um teste de hipótese é definido como:
    * Hipótese nula(H0):  Assumida como verdadeira(é aquilo que queremos testar)
    * Hipótese alternativa(HN): considerada quando H0 é falha!
* Testes de média: 
  * Ex: Uma garrafa de cerveja padrão tem 600ml. Com uma amostragem de 50 garrafas podemos continuar dizendo que uma garrafa possui 600ml?
    * Aqui pegaríamos a média das 50 garrafas pra infeir se a minha amostra tem 600ml ou algo próximo dentro do meu intervalo de significância;
* Testes de proporção:
  * Uma fábrica declara que menos de 5% da sua produção vem com defeito. Em uma mostra de 100 unidades encontramos 100 defeituosas. Os números da fábrica estão corretos?
* Erro tipo 1: Falso positivo!
* Erro tipo 2: Falso negativo!

## P Valor
* Probabilidade de obter ume estatística de testes igual ou maior que a observada em uma amostra para H0;
* Quanto menor o p-valor maios a chance de se rejeitar a hipótese nula
* Define-se o alpha e o p-valor antes do experimento;

## Tipoas de Teste
* T-student: Usado para comparar dois grupos utilizando média;
* Shapiro-wilk: teste de normalidade
  * Usa uma amostra da população pra validar se a mesma está distribuída em uma normal
  * H0: Amostra provém de uma normal;
  * HN: Amostra não provém de uma normal
* Jarque-Bera: teste de normalidade
  * Valida se existe desvio padrão
  * Curtosis e assimetria
  * H0: Amostra provém de uma normal
  * HN: Amostra não provém de uma normal
* Gráfico Q-Q
  * Gráfico Quantil-Quantil
  * Compara a distribuição de duas probabilidades
  * Entre duas variáveis
