Documentation complète du script

Titre: Guide d'utilisation du script [Nom du Script]

Introduction:
Le script Auto.py est un outil puissant conçu pour faciliter l'installation, la configuration et le lancement
Ce guide détaillé vous accompagnera à travers chaque étape, de l'installation initiale à l'exécution réussie du script.

1- Installation de Git :
Si vous n'avez pas encore Git installé sur votre ordinateur, vous devez le faire en suivant ces étapes :

Téléchargez Git à partir du site officiel : 
Suivez les instructions d'installation pour votre système d'exploitation.



2- Clonage du dépôt Git :
	Une fois Git installé, vous pouvez cloner le dépôt Git du projet que vous souhaitez installer sur votre ordinateur :
Ouvrez une fenêtre de terminal ou de ligne de commande.
Utilisez la commande cd pour naviguer vers le répertoire où vous souhaitez cloner le projet.
Exécutez la commande suivante pour cloner le dépôt Git :
 - git clone <url_du_depot_git>
 
Une fois le clonage terminé, vous pouvez accéder au répertoire du projet en utilisant la commande cd. Par exemple :
 - cd nom_du_projet

3- Configuration de l'environnement virtuel (venv):
	Ouvrez une nouvelle fenêtre de terminal ou de ligne de commande.
Installez le module venv si ce n'est pas déjà fait : 
 - pip install virtualenv
   
Créez un nouvel environnement virtuel en exécutant la commande suivante :
 - python -m venv <chemin_vers_env>

Remplacez <chemin_vers_env> par le chemin où vous souhaitez créer votre environnement virtuel. Par exemple :
 - python -m venv myenv
 - 
Activez l'environnement virtuel :
Sur Windows :
 - <chemin_vers_env>\Scripts\activate
  
Sur macOS et Linux :
 - source <chemin_vers_env>/bin/activate
   
Une fois l'environnement virtuel activé, vous pouvez installer les dépendances spécifiques à votre projet, y compris Selenium, en utilisant pip.
Assurez-vous que l'environnement virtuel est activé avant d'installer les dépendances :
 - pip install selenium

4- Ajout de vos infoarmation personnelle pour la recherche : 
Configuration:

	a- Informations Telegram Bot:
				Remplacez la valeur de telegram_bot_token par le jeton de votre bot Telegram. 
	Si vous n'avez pas encore créé de bot Telegram, suivez les instructions officielles pour en créer un et obtenir le jeton.
	Remplacez la valeur de telegram_group_chat_id par l'identifiant de votre groupe Telegram où vous souhaitez recevoir les notifications. 
 	Vous pouvez trouver l'identifiant du groupe en utilisant des outils en ligne ou en demandant à votre bot Telegram.
	
	b- URL de la page à surveiller:
 				Modifiez la valeur de url_page pour correspondre à l'URL de la page de recherche de logements que vous souhaitez surveiller.
  Mot spécifique à rechercher:
	Si vous souhaitez rechercher un mot spécifique sur la page pour déclencher une notification, modifiez la valeur de mot_specifique. Sinon, laissez-la vide pour rechercher un mot spécifique dans la page.

 
5- Lancement du projet:
Assurez-vous que vous êtes dans le répertoire du projet où vous avez cloné le dépôt Git.
Selon le type de projet, vous pouvez lancer l'application de différentes manières. Si c'est une application web, vous pouvez avoir besoin d'exécuter un serveur de développement. Si c'est une application Python, vous pouvez exécuter le script principal, etc.
Pour lancer l'application, suivez les instructions spécifiques au projet. Cela pourrait impliquer d'exécuter une commande spécifique ou de cliquer sur un bouton "Run" dans un IDE ou un environnement de développement intégré.


6- Arrêt de l'application:
Une fois que l'application est en cours d'exécution, vous pouvez l'arrêter en utilisant "Ctrl+C" dans le terminal ou l'invite de commande où vous avez lancé l'application.
Appuyez sur "Ctrl+C". Cela enverra un signal d'interruption à l'application, ce qui devrait normalement la fermer proprement.
