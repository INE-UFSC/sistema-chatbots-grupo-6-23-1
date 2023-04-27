# Sobre:
O código acima simula uma empresa que cria chatbots, e permite a conversação com bots simples (cujas perguntas e respostas já são pré-definidas no sistema) e de bots com inteligência artificial, através de uma interação com o ChatGPT, da OpenAI. O software é puramente didático e sem fins lucrativos.
Note que alguns procedimentos, que estão descritos à seguir, precisam ser realizados para que se possa utilizar a integração com o ChatGPT.

# Como utilizar a integração como ChatGPT:
 1. Clone o repositório
 
 2. Conecte-se ao sistema do ChatGPT em https://platform.openai.com/docs/api-reference
 
 3. Acesse o link https://platform.openai.com/account/api-keys 
 
 4. Crie uma chave no botão `+ Create new secret key` com qualquer nome que desejar
 <br/><br/> ![image](https://user-images.githubusercontent.com/42248953/234928869-716eb5f6-925a-439e-b772-65cc8c6949ff.png)
 
 5. Copie a chave e cole-a no arquivo `py_env.py` onde está escrito `'your_key_here'`
 <br/><br/> ![image](https://user-images.githubusercontent.com/42248953/234929784-6641ea7a-a42e-43aa-8138-48c3cca1e4a9.png)
 
 6. Por fim, execute o arquivo `app.py` para iniciar o programa
 
# Observações:

1. Para adicionar uma nova instância de `BotChatGpt`, pasta importar a classe, instanciar um objeto que recebe apenas o nome de algum personagem de sua escolha.

2. Note que as mensagens geradas pelas instâncias de `BotChatGpt` demoram mais para aparecer na tela, isso acontece pois há uma requisição em andamento e o sistema não tem suporte para funções `async` (assíncronas).


---


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/raIOteMi)
# ine-5404-sistema-chatbot-template

Template (v0) do Sistema Chatbot - atividade síncrona - INE5404

Veja abaixo um exemplo de funcionamento do sistema:

![image](https://user-images.githubusercontent.com/17619917/109540740-a6b2ef80-7aa1-11eb-8b59-8e79e56d5a68.png)

A partir do diagrama de classes fornecido e usando a estrutura de arquivos deste repositorio:

1) Realizar a implementação do sistema com ao menos dois bots de personalidades diferentes
2) Fornecer as implementações de bot a outros grupos e tentar integrar outras implementações de bot no seu sistema
