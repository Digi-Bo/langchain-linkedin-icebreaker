# Importation de la classe SerpAPIWrapper depuis le module langchain.utilities
from langchain.utilities import SerpAPIWrapper


# Définition d'une classe CustomSerpAPIWrapper qui hérite de SerpAPIWrapper
class CustomSerpAPIWrapper(SerpAPIWrapper):
    # Initialisation de la classe
    def __init__(self):
        # Appel du constructeur de la classe parente
        super(CustomSerpAPIWrapper, self).__init__()

    # Définition d'une méthode statique pour traiter la réponse provenant de SerpAPI
    @staticmethod
    def _process_response(res: dict) -> str:
        """Traite la réponse de SerpAPI."""

        # Vérification si la réponse contient une erreur
        if "error" in res.keys():
            raise ValueError(f"Erreur reçue de SerpAPI : {res['error']}")

        # Différentes conditions pour extraire les informations pertinentes de la réponse
        if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
            toret = res["answer_box"]["answer"]
        elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
            toret = res["answer_box"]["snippet"]
        elif (
            "answer_box" in res.keys()
            and "snippet_highlighted_words" in res["answer_box"].keys()
        ):
            toret = res["answer_box"]["snippet_highlighted_words"][0]
        elif (
            "sports_results" in res.keys()
            and "game_spotlight" in res["sports_results"].keys()
        ):
            toret = res["sports_results"]["game_spotlight"]
        elif (
            "knowledge_graph" in res.keys()
            and "description" in res["knowledge_graph"].keys()
        ):
            toret = res["knowledge_graph"]["description"]
        elif "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]
        else:
            # Si aucune condition n'est satisfaite, retourner une chaîne indiquant qu'aucun bon résultat de recherche n'a été trouvé
            toret = "Aucun bon résultat de recherche trouvé"

        return toret


# Définition d'une fonction pour obtenir l'URL du profil LinkedIn ou Twitter
def get_profile_url(name: str):
    """Recherche la page de profil LinkedIn ou Twitter."""

    ### Problème avec la réponse de SerpAPIWrapper() : je n'obtiens pas l'url de Linkedin 
    search = SerpAPIWrapper()


    # Création d'une instance de la classe CustomSerpAPIWrapper
    # search = CustomSerpAPIWrapper()

    # Exécution de la recherche
    res = search.run(f"{name}")

    return res
