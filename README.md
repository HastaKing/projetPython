# HowTo

Download data here :

	- http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/
		--> Rename as data_activity.json

	- http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
		--> Rename as data_installation.json

	- http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/
		--> Rename as data_equipment.json

	Put these files in a folder named data/ (the path will be projetPython/data/*.json)

Generate dataBase :

	python3 services/json_service/json_to_activity.py
	python3 services/json_service/json_to_equipment.py
	python3 services/json_service/json_to_installation.py


Link dataBase :

	python3 services/data_service/data_link.py


Launch the cherryPy server :

	python3 services/web_service/cherryPyServer.py


Acces in the web browser :

	localhost:8080


Have some fun !

Author : Jonas Bouscharain, 2015