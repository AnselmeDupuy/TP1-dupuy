| Principe | Fichier et ligne | Le symptôme observable | La conséquence concrète |
|---|---|---|---|
|S|facture.py, ligne 33|appelle de plusieur acteurs|révision de la fonction pour 3 raisons différentes|
|O|tarif.py, ligne 39|function fermé à la modification simple|refactorisation|
|L|abonnements.py, ligne 48|héritage inutile|raise une exception que le contrat interdit|
|I|passerelles|interface non-conforme|augmentation des tests|
|D|facture.py, ligne 7|injectino du protocole SMTP|besoin serveur pour test|


| Demande | Fichiers à rouvrir | Fonctions à modifier | Tests existants à rejouer |
|---|---|---|---|
|Ajoute formule découverte, 4€ par poste|tarifs.py|prix_par_poste|test_chaque_formule_a_son_prix_par_poste|
|Ajout code promo: RENTREE -10%|tarifs.py|appliquer_code_promo|test_un_code_promo_inconnu_est_refuse|
|Ajout troisième palier de remise sur volume : 30 % pour > 200 postes.|tarifs.py|taux_de_remise_volume|test_la_remise_volume_suit_les_paliers|


./depart/facturation/abonnements.py:3:from dataclasses import dataclass
./depart/facturation/abonnements.py:4:from datetime import date
./depart/facturation/facture.py:3:from dataclasses import dataclass
./depart/facturation/facture.py:4:from datetime import date, datetime
./depart/facturation/facture.py:6:from facturation.abonnements import Abonnement
./depart/facturation/facture.py:7:from facturation.passerelles import ClientSMTP
./depart/facturation/facture.py:8:from facturation.tarifs import montant_hors_taxe, montant_toutes_taxes
./depart/facturation/passerelles.py:3:from abc import ABC, abstractmethod
./depart/facturation/tarifs.py:3:from facturation.abonnements import (
