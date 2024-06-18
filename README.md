# Projeto: Gerador de Orçamentos

## Descrição

Bem-vindo ao **Gerador de Orçamentos**, um aplicativo desenvolvido em Python que facilita a criação de orçamentos profissionais. Utilizando bibliotecas como `tkinter`, `fpdf`, `os`, `sys` e `PIL`, o software permite inserir informações essenciais do projeto e gera um documento de orçamento detalhado. Esse documento inclui uma descrição do projeto, horas estimadas, valor da hora de trabalho, prazo de entrega, e o valor total do orçamento.

## Funcionalidades

- **Interface Intuitiva**: Desenvolvido com `tkinter`, o aplicativo oferece uma interface amigável e fácil de usar.
- **Geração de PDFs**: Com a biblioteca `fpdf`, o orçamento é gerado em um formato PDF profissional.
- **Manipulação de Arquivos**: Utiliza `os` e `sys` para gerenciar arquivos e caminhos de maneira eficiente.
- **Manipulação de Imagens**: Integração com `PIL` para adicionar logotipos ou outras imagens ao orçamento.

## Campos do Formulário

- Descrição do Projeto: Informe uma descrição detalhada do projeto.
- Horas Estimadas: Informe a quantidade de horas estimadas para a conclusão do projeto.
- Valor da Hora de Trabalho: Informe o valor cobrado por hora de trabalho.
- Prazo de Entrega: Informe o prazo de entrega do projeto.
- Valor Total: Calculo com preço final.

## Geração do Orçamento

Após preencher todos os campos, clique em "Gerar Orçamento". O aplicativo irá:

- Calcular o valor total do orçamento (Horas Estimadas x Valor da Hora de Trabalho).
- Gerar um documento PDF a partir de um template com todas as informações inseridas e o valor total calculado.
- Salvar o documento PDF em um diretório especificado.

Criado por: Bruno Abdalla Guimarães