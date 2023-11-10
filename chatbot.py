import openai

openai.api_key = "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"


# Funcao para gerar texto a partir do modelo de linguagem
def gera_texto(texto):
    # Obtém a resposta do modelo de linguagem
    response = openai.Completion.create(

        engine="text-davinci-003",

        promp=texto,

        max_tokens=150,

        n=5,

        stop=None,

        temperatura=0.8
    )

    return response.choices[0].text.strip()


# Funcao principal do programa em Python

def main():
    print("Bem-vindo ao Projeto GPT Chatbot")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    # Loop
    while True:
        # Coleta a pergunta digitada pelo usuário.
        user_message = input("Você: ")

        # Se a mensagem for "sair" finaliza do programa
        if user_message.lower() == "sair":
            break

        # Coloca a mensagem digitada pelo usuário na variável Python chamada gpt_prompt.
        gpt_prompt = f"\nUsuário: {user_message}\nChatbot:"

        # Obtêm a resposta do modelo executando o funcao gera_texto.
        chatbot_response = gera_texto(gpt_prompt)

        # Imprime a resposta do chatbot
        print(f"\nChatbot: {chatbot_response}")


# Execução do programa (bloco main) em Python

if __name__ == "__main__":
    main()
