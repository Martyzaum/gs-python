# Sistema de Agendamento de Exames

Este é um simples sistema de agendamento de exames em Python. O código é interativo e orienta o usuário através do processo de inserção de informações pessoais, escolha do tipo de exame e agendamento da data. Aqui está uma explicação passo a passo do funcionamento do código:

## Funcionalidades Principais:

1. Obtenção de Informações do Usuário:

- Solicitação do nome, idade e cidade do usuário através da função input.
- Exibe uma mensagem de boas-vindas com as informações fornecidas.

2. Escolha do Tipo de Exame:

- Apresenta opções de exames (exame de sangue, raio-X, ultrassom).
- Usa um loop while para garantir que o usuário insira uma opção válida.
- Limita a quantidade de tentativas para 5, encerrando o programa se exceder esse limite.
- Exibe a escolha do usuário.

3. Agendamento da Data do Exame:

- Apresenta opções de data para o exame (três dias consecutivos a partir da data atual).
- Usa um loop while para garantir que o usuário insira uma opção válida.
- Limita a quantidade de tentativas para 5, encerrando o programa se exceder esse limite.
- Calcula a data agendada com base na escolha do usuário.

4. Mensagens de Confirmação e Encerramento:

- Exibe mensagens de confirmação, agradecendo ao usuário e informando a data do exame agendado.
- Se o número máximo de tentativas for atingido em qualquer etapa, o programa encerra com uma mensagem apropriada.

## Execução do Código:

- O usuário executa o código Python em um ambiente compatível.
- As informações pessoais são solicitadas e exibidas.
- O usuário escolhe o tipo de exame e uma data disponível.
- O programa confirma o agendamento ou encerra se o número máximo de tentativas for atingido.

## Requisitos:

- Python 3.x instalado no sistema.

## Como Executar:

- Abra um terminal ou prompt de comando.
- Navegue até o diretório onde o código está salvo.
- Execute o seguinte comando: python nome_do_arquivo.py (substitua nome_do_arquivo pelo nome real do arquivo Python).

## Considerações Finais:

Este sistema de agendamento de exames é uma aplicação simples, mas eficaz, para interação com o usuário. Ele utiliza conceitos básicos de entrada de dados, estruturas de controle de fluxo (if, elif, else), loops while, manipulação de datas com o módulo datetime e formatação de strings. Este código pode ser um ponto de partida para projetos mais complexos ou pode ser expandido para incluir mais recursos, como armazenamento de dados, opções adicionais de exames, etc.

Guilherme Fernandes de Freitas RM554323
Lucas de Freitas Pagung RM553242