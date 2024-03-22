import time
from selenium import webdriver
import requests

# Vos informations Telegram Bot
telegram_bot_token = '6539310494:AAHwrGsQdB8nlPUXGejDZRPHVvqtg2tNxDQ'
telegram_group_chat_id = '-4058022836'  # Remplacez par l'identifiant de votre groupe

# URL de la page vérifier
url_page = "https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.2235574_49.9505487_2.3457767_49.846837"

# Mot spécifique à rechercher sur la page
mot_specifique = "Aucun logement trouvé"

# Configuration du navigateur Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Pour exécuter le navigateur en arrière-plan

# Boucle infinie
while True:
    # Accéder à la page
    driver = webdriver.Chrome(options=options)
    driver.get(url_page)

    # Vérifier si le mot spécifique est présent sur la page
    if mot_specifique in driver.page_source:
        print("RAS (Rien à signaler)")

    if ' ' in driver.page_source:
        print("Aucun élements retrouve")

    else:
        print(f"Mot spécifique '{mot_specifique}' non trouvé. Envoi d'un message sur le groupe Telegram...")

        # Message à envoyer
        message_body = f"Depeche toi nous avons trouvé de nouveau appartements sur Lille via le crouss: {url_page}"

        # URL pour l'envoi du message Telegram vers le groupe
        telegram_api_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'
        params = {'chat_id': telegram_group_chat_id, 'text': message_body}

        # Utiliser requests pour envoyer le message
        response = requests.get(telegram_api_url, params=params)

        print("Message envoyé avec succès.")

        # Après l'envoi de message
        #print(f"Réponse de l'API Telegram : {response.json()}")

    

    # Fermer le navigateur
    driver.quit()

    # Attendre 60 secondes avant la prochaine itération
    time.sleep(60)

   