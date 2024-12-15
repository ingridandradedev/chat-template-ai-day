# Streamlit LangFlow Agent Tester Template

Este é um projeto simples em **Streamlit** que permite às pessoas rapidamente testar e disponibilizar uma URL pública para seus agentes desenvolvidos no **LangFlow**. 

A aplicação fornece uma interface de chat básica, onde o usuário pode interagir com seu agente configurado no LangFlow, passando mensagens em texto e recebendo respostas.

## Funcionalidades

- **Interface de Chat**: Permite enviar mensagens para o agente e receber respostas.
- **Configuração Rápida**: Integre seu agente do LangFlow apenas preenchendo o arquivo `.env`.
- **Histórico de Mensagens**: O histórico da conversa é exibido na interface.
- **Pronto para Uso**: Inclui um modelo básico que pode ser facilmente customizado.

---

## Configuração do Ambiente

Para executar o projeto, basta preencher o arquivo `.env` com as informações do seu agente LangFlow. Este arquivo já está incluído no projeto e precisa ser ajustado com os valores corretos.

### Exemplo de Conteúdo do Arquivo `.env`

Abra o arquivo `.env` e preencha os campos conforme o exemplo abaixo:

```env
# URL da API do LangFlow
LANGFLOW_API_URL=https://sua-api-langflow.com/api/v1

# Token de autenticação da API
LANGFLOW_API_TOKEN=seu_token_api_aqui

# Dados do agente (em formato JSON)
LANGFLOW_API_DATA={"input_value": "message", "output_type": "chat", "input_type": "chat"}

# Título do agente (exibido no Streamlit)
AI_AGENT_TITLE=Meu Agente LangFlow

# Descrição do agente (exibida no Streamlit)
AI_AGENT_DESCRIPTION="Este é um exemplo de agente desenvolvido no LangFlow."

## Limitações

- **Entrada Limitada a Texto**: O chat suporta apenas entradas textuais, sem suporte para upload de arquivos, envio de imagens ou outros tipos de dados.
- **Saídas Simples**: As respostas geradas pelo agente são textuais e não incluem elementos sofisticados, como gráficos ou visualizações.
- **Casos Simples**: Ideal para agentes que já possuem, no LangFlow, acesso integrado a todas as informações necessárias, sem necessidade de inputs adicionais.

Este projeto é indicado para testes rápidos e agentes configurados para lidar com interações básicas.

