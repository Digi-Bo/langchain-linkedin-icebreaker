# Importation de divers modules et fonctions
from tools.tools import get_profile_url
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType


# Définition d'une fonction lookup qui prend un nom en argument et renvoie un URL de profil LinkedIn
def lookup(name: str) -> str:
    # Initialisation du modèle de chat avec OpenAI (GPT-3.5 Turbo) avec une température de 0
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Création d'un modèle de prompt
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                    your answer should contain only a url"""

    # Liste d'outils disponibles pour l'agent, ici un seul outil pour obtenir l'URL de LinkedIn
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the Linkedin Page URL",
        ),
    ]

    # Initialisation de l'agent avec les outils, le modèle et le type d'agent
    agent = initialize_agent(
        tools_for_agent, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    # Initialisation du modèle de prompt avec les variables à remplacer
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    # Exécution de l'agent pour obtenir le nom d'utilisateur LinkedIn
    linkedin_username = agent.run(prompt_template.format_prompt(name_of_person=name))

    # Renvoi du nom d'utilisateur LinkedIn
    return linkedin_username
