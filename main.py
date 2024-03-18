from opgg.opgg import OPGG
from chatgpt.chatgpt import ChatGPT
from chatgpt.prompt import chat_gpt_messages
import config
openai_api_key = config.OPENAI_API_KEY


def main():    
    summoner_name = "ClockBomb-lol"
    region = "euw"

    opgg = OPGG(region, summoner_name)
    opgg.get_summoner_page()

    print(opgg)
    info = str(opgg)

    filled_user_prompt = chat_gpt_messages[1]["content"].substitute(info=info)
    text_generator = ChatGPT(openai_api_key)

    generated_roast = text_generator.generate(filled_user_prompt)
    print("\nGenerated Roast:")
    print(generated_roast)





if __name__ == "__main__":
    main()