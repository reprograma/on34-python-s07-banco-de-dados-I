BANCO DE DADOS Afetos:

Eu sou uma pessoa Não-Monogâmica (NM) e em razão do tipo que trabalho que tinha (embarcava 42 dias e em seguida tinha 42 dias de férias) dispunha de muito tempo para meus afetos (lê-se pela sociedade convencional como: amigues, familiares e relações afetivas-sexuais). No entanto, no momento estou me dedicando a realizar uma transição de carreira, logo disponho de menos tempo, e com isso preciso gerenciar melhor os encontros e momentos de atenção que dedico aos meus entes queridos.

Sendo assim vou organizar a tabela de Afetos e os seus respectivos dados; outra com os tipos de encontros; e o resgistro dos dates em si.

Quais os afetos que eu tive mais encontros?
Quem eu possivelmente estou negligenciando (menos encontros)? Ainda que não seja necessária equivalência.
Qual o tipo de enocntro que mais tenho?

Estruturei uma arquitetura com três entidades contando com chaves primárias e estrangeiras para solucionar o problema inicial.

Criei toda a estrutura desenhada e populei as tabelas citadas.

Mostrei ajustes que teve que fazer depois da estrutura completa. Usando o metodo UPDATE, DROP ou ALTER para modificar sua estrutura.

Criei consultas para entender melhor os dados, ao menos 3 consultas relacionadas as dúvidas iniciais.

Com qual afeto tive mais encontros?
Onde ocorre a maioria dos encontros?
Qual o tipo de enocntro que mais ocorre?

Essas foram as questões que consegui responder, e não exatamente, mas apresentando o resumo dos dados. as perguntas que fiz quando idealizei o banco de dados, eu não consegui responder, pois não tinha ferramentas suficientes.

Eu gostaria de ter colocado a tabela do tipo N:N, pois um encontro pode ter vários afetos, assim como os afetos podem ter vários encontros. Mas não consegui.


banco de dados"Bicho é meu Vicio" 

O negócio da empresa é prestar os serviços de banho, corte e adestramento para todo o tipo de animal, mas especializado em aves, mamiferos, répiteis e peixes. Em seus resgistros, gostariam de guardar informações sobre os seus clientes humanoides e não humanóides e qual e quando aconteceu um atendimento deles na loja.

Com isso, esperam entender melhor seu fluxo de vendas, quais os serviços mais demandados e os tipos de bichos que mais os procuram.

Criei seis entidades de tabelas, seus campos e atributos, contando com chaves primárias e estrangeiras para solucionar o problema inicial.

Criei toda a estrutura desenhada e populei as tabelas citadas.

Criei consultas utilizando:

SELECT = O que deve ser selecionado e consultado (se preenche com nome de colunas e funções)
FROM = Base onde os dados estão armazenados (se preenche com nome de tabelas)
WHERE = Filtros que devem ser aplicados na consulta (se preenche com nome de colunas e suas condições)
GROUP BY = Agregações que devem ser aplicadas a consulta (se preenche com nome de colunas)
ORDER BY = Ordenações que devem ser aplicadas a consulta (se preenche com nome de colunas)
LIMIT = O tamanho máximo do resultado (se preenche com numeros inteiros)

Respondi as necessidades de negócio:

Qual o serviço mais usado da loja?
Qual o tipo de Bicho mais popular?
Qual a receita de vendas dos dados registrados?
Quais os ids mais importantes que preciso?