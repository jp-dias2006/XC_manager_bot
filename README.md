# XC_bot

Bot do Telegram para gerenciar a recepção de usuários e assinaturas do grupo VIP.

## Funcionalidades
- Gerenciar recepção de novos usuários
- Gerenciar assinaturas do grupo VIP

## Configuração de ambiente
- Renomeie `.env.example` para `.env` e preencha com seu token:
  ```ini
  TELEGRAM_BOT_TOKEN=seu_token_aqui
  ```

## Como rodar

1. Instale as dependências:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Execute o bot:
   ```powershell
   python -m XC_bot.main
   ```

## Testes

Para executar os testes com pytest:
```powershell
python -m pytest 
```
