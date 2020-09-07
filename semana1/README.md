# Introdução

* *Instalar o app da Codenation*
* *Assistir as aulas de Git*

# Conteúdos Opcionais

## Princípios de Reprodutibilidade e Boas Práticas de Código

* *Capacidade de reproduzir uma análise ou esperimento de forma consisente em um momento futuro, dispondo dos mesmos dados e ferramentas;*
    * Isso não significa que o resultado está certo, apenas que ele é condizente com o método proposto;
* A reprodutibilidade é uma condição *necessária*, mas *não suficiente* para a credibilidade da análise;
* O reaproveitamento de materiais disponibilizados é muito importante para construir conhecimento;
* Para Data Science e Estatística, *reprodutibilidade é fundamental!*;
* *Qualidade de Código* é essencial;
* *Jupyter* é uma ferramenta bastante interessante para data science;

## Ambiente Python

* Assistir o vídeo de Ambiente com Python;

## Git

* Assistir os vídeos de Git;

## Clean Codding e Logging;

* Importar somente os métodos que vamos usar das bibliotecas;
* Dar nomes que consigam transmitir a mensagem do que um método, variável, classe ou parâmetro significam;
* Usar anotations sempre que possível para indicar o que cada componente do código significa/faz;
* Para python, sempre utilizar o `if __name__ == '__main__'`;
* Um trecho de código é *estatísticamente mais lido do que escrito*;
* É importante convencionar um idioma(não é mandatório);
* É importante não ter nomes muito verbosos para métodos, classes, variáveis e parâmetros;
    * O nome deve ser conciso ao máximo de forma que tenha o menor tamanho possível passando a ideia da função daquilo que estamos nomeando;
* Uma dica legal é manter a simetria na nomeação das variáveis 
    * Ex: se tenho um método `open_file()` o método para fechar o arquivo deve ser algo como `close_file()`; 
* Quando a variável for boolean, tentar colocar nomes que reflitam o significado delas
    * Exemplo: quando tenho uma variável que denota o sucesso de alguma coisa, posso nomeá-la como `success = true`;
* *Ver o loguru para logging em python*;



## Unit Tests

* Testes hoje são obrigatórios;
* *São a única garantia que o nosso código faz o que ele deveria fazer*;
* Testes automatizados tem vários níveis que vão desde testes unitário(testa uma porção pequena por vez) até testes de integração(que testa o comportamento esperado do sistema como um todo, nos preocupando com as interações entre classes do nosso software);
* Testes end2end
* *Estudar Mock*;
* Testes devem ser baseados no comportamento da classe e não na programação;
* Ao utilizar TDD, eu escrevo os testes antes de programar, isso garante que a gente implemente o código da forma mais desacoplada possível;
* O TDD ajuda a ter classes mais consisas e código mais limpo;
* *Unit Test* e *PyTest*;
* Os métodos devem começar com `test_nome_do_metodo`;
* É possível criar uma classe que executa vários métodos. Ela deve começar com ou `TestNomeDaClasse`
* *@pytest.fixture*: essa annotation executa sempre essa operação priemeiro antes de executar cada um dos os testes e então disponibiliza esse valor para o teste com injeção de dependências;
    * É possível parametrizar o fixture para ser executado uma única vez no script;
* *@pytest.parametrize*: permite paramtrizar os testes a serem rodados de forma automática;

* *Pesquisar mais sobre TDD*

## Docker

* Assistir aos vídeos sobre Docker

# Data Science - Módulo 1

## O que é ciência?

* Observações;
* Raciocínio dedutivo sobre fenômenos observados;
* *Metodologia* 
    * O discurso do método de Descartes;
* Edgar Morin
    * *Pensamento Complexo*: Tenta compreender os fenômenos observados como um todo e não como fenômenos isolados
    * *Fenômeno da variável omitida*: estudar;
    * Visão sistemina e multidisciplinar do fenômeno observado;
* Método Científico:
    * Fazer uma observação;
    * Formular uma Hipótese;
    * Realizar um experimento;
    * Analisar os dados;
    * Reportar as descobertas;
    * COnvidar terceiros para replicar os resultados.
* Ciência de Dados deve resolver problemas reais dentro do negócio utilizando métodos e metodologias científicas;

## Bigdata

* Explosão no volume de dados gerados nos últimos anos;
* Dificuldade 
* 5 V's do Bigdata
    * Velocidade: velocidade que vc precisa que estes dados sejam transformados ou que cheguem até você;
    * Volume: O volume de dados que chega;
    * Variedade: quais os formatos dos dados que chegam;
    * Veracidade: Como garantir que os dados são verídicos;
    * Valor: O processo de Bigdatea deve gerar valor para a empresa. A informação gerada deve gerar valor!
* Governança de Dados: 
    * Para onde eu vou(em termos de negócio), como vou, quando vou?
    * Que dados são necessários?
    * COmo obter esses dados e como mantê-los?
    * Quais áreas serão prioritárias no tratamento dos dados baseado na estratégia de negócio?

## Papéis - Projeto de Dados

* Quem são as pessoas responsáveis por entregar valor em um projeto de dados?
    * Engenheiro de Dados;
    * Data Science Manager;
    * DataArchtect;
    * Machine Learning Engineer;
    * Data Engineer;
    * Decision Scientists;
    * Statistician;

## Tipos de Soluções de Análise

* Solução descritiva:
    * Descrever o que existe;
    * *O que aconteceu?*;
* Solução Diagnóstica:
    * Ocorre depois da solução descritiva;
    * Descreve os porquês;
    * *Porque o fato ocorreu?*;
    * Esse tipo de análise deve estar em constante contato com as outras áreas do negócio!;
* Solução Preditiva:
    * Descreve o que vai acontecer/existir no futuro;
    * *O que vai acontecer?*
    * Aqui vamos usar o passado para predizer o futuro!
    * Previsão e Predição
        * Subconjunto da predição vinculado ao tempo;
        * Forma genérica de como um fato seria antes de sua ocorrência;
* Solução Prescritiva:
    * Recomenda a tomada de decisão;
    * usando previsão/predição remomenda uma ação;
    * *O que eu vou fazer?*

## Tipos de Problema
* *O que a ciência de dados resolve?*;
* Classificação Binária:
    * Prevê um resultado binário(duas classes possíveis);
    * Exemplo: *Regressão Logística*;
* Classificação multiclasse
    * Permitem gerar previsões para várias classes(*Prever um entre mais de dois resultados*);
    * Exemplo: *Regressão Logística multinomial*;
* Regressão
    * Modelo de Regressão
    * Preveem um valor numérico
    * Exemplo: *Regressão Linear*;
* Agrupamento:
    * Modelo aprende grandes grupos / divisão dos dados;
    * Retorna um grupo;
    * Exemplo: *KMeans*;
* Sistemas de Recomendsação
    * Sugere ou recomenda algo ao usuário
    * Retorna uma sugestão
    * Exemplos: *Collaborative Filter / Content Based*

## Tipos de Aprendizado
* Supervisionado
    * São apresentados ao algoritmo a saída esperada através de exemplos. O objetivo é aprender uma regra geral que mapeia as entradas para as saídas esperadas;

* Não Supervisionado
    * Nenhum tipo de label é passado. O objetivo é que o algoritmo descubra padreões para separar os dados

* Semi-Supervisionado

* Reinforcement Learning

## Maturidade com Analytics
* Maturidade dos Dados:
    * Como a empresa lida com os seus dados:
        * Dados crus: Pouca maturidade(dados não geram valor);
        * Informação: Os dados começão a trazer valor para a organização mas precisão ser trabalhados manualmente;
        * BI: Organização já tem uma visão bacana sobre o passaso. Tem dashboards, ETL, Governança dos dados e etc;
        * Advanced Analytics: Conhecimento profundo sobre os dados. Utiliza soluções preditivas;
* Maturidade Analítica:
    * Tipos de solução de análise
        * A empresa entende *o que aconteceu, porque aconteceu, o que vai acontecer e o que eu devo fazer*;

## O processo da Ciência de Dados
* Método Científico:
    * Entender o problema e então formular uma hióótese;
    * Definir a metodologia e realisar os experimentos;
    * Analisar os resultados e compartilhá-los para que outras pessoas possam reproduzí-los.
* Processo da Ciência de Dados:
    * Entender o problema do negócio;
        * Realizar entrevistas, analisar documentos e entender realmente como funciona o negócio e o problema a ser resolvido;
    * Definir o problema a ser analisado;
        * Definir o problema a ser solucionado e transformá-lo em um problema de dados definindo os KPI's para a sua avaliação;
    * Definir a stack de tecnologia a ser utilizada;
        * Definir as tecnologias que serão utilizadas no projeto
    * Entender os dados(Análise Exploratória e Visualização dos Dados);
        * Explorar as correlações entre as variáveis;
        * Testes de Hipótese;
    * Preparação dos dados;
        Feature Selectione Feature Engineering;
    * Modelagem dos Dados;
        * Avaliação das melhores métricas e modelos para o problema do negócio
    * Avaliação e Feedback;
        * Como mostrar esses reultados e avaliação dos resultados em diferentes cenários
    * Deploy em Produção; 
        * Deploy do modelo para produção
    * Feedback
        * Avaliação do modelo no mundo real;