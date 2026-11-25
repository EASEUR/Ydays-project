# Journal de bord - Task Manager sur serveur

Une entrée par jour de travail : ce qui a été fait, les difficultés, la suite.

---

## Jour 1 - 16 octobre 2026

### Fait
- Lecture du sujet et des barèmes (étape 1 et étape 2).
- Liste des tâches de l'étape 1.
- Création du `README.md` (présentation du projet) et du `JOURNAL.md`.

### Difficultés
- Aucune pour le moment.

### Prévu pour le prochain jour
- Créer le dépôt Git et la structure du projet (`agent/`, `server/`).
- Choisir les technologies.
- Écrire l'agent v1.

---

## Jour 2 - 25 novembre 2026

### Fait
- Création du dépôt Git, du `.gitignore` (`.venv/`, `__pycache__/`, `*.db`) et de la structure du projet.
- Choix des technologies : Python + `psutil` pour l'agent, FastAPI pour l'API, SQLite pour la base, échanges en JSON via HTTP.
- Agent v1 (`agent/agent.py`) : relève le CPU, la mémoire, le disque et les 10 processus les plus gourmands (nom, PID, CPU, RAM) toutes les 10 secondes, avec gestion des erreurs.
- API FastAPI (`server/main.py`) : route `POST /mesures` avec validation du format et stockage en base SQLite, route `GET /mesures` pour consulter les dernières mesures.
- Agent branché sur l'API : il envoie ses vraies données avec `requests`, et continue de tourner si le serveur est injoignable.
- Test de bout en bout en local : agent → API → base fonctionne.

### Difficultés
- Erreur `No module named psutil` : le venv n'avait pas de `pip`. Résolu en recréant le venv avec `python3 -m venv .venv`.
- La route `/` renvoyait « Not Found » : normal, seule `/mesures` est définie (la page de test est sur `/docs`).

### Prévu pour le prochain jour
- Dessiner le schéma d'architecture (flux, ports, choix justifiés).
- Installer le serveur sur une VM ou un VPS, joignable depuis une autre machine.
- Lancer l'API comme service `systemd` (redémarrage automatique).
- Compléter le README (installation) et préparer la présentation de l'étape 1.

---

## Modèle pour les jours suivants

```
## Jour N - JJ/MM/AAAA

### Fait
-

### Difficultés
-

### Prévu pour le prochain jour
-
```