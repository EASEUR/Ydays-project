# Task Manager sur serveur

Un gestionnaire de tâches à distance : on surveille l'état d'une ou plusieurs machines depuis n'importe où, à travers un navigateur ou une API.

## Le projet en bref

Quand on ouvre le gestionnaire de tâches d'un ordinateur, on voit ce qu'il fait en ce moment : l'usage du processeur, de la mémoire, du disque, et les programmes qui tournent. Ce projet fait la même chose, mais **à distance** : on peut consulter ces informations sans être devant la machine.

## Comment ça marche

Le projet se compose de trois parties :

1. **L'agent** : un petit programme installé sur la machine à surveiller. Il relève régulièrement ses informations (CPU, mémoire, disque, processus les plus gourmands) et les envoie au serveur.
2. **Le serveur** : il reçoit les données de l'agent, vérifie qu'elles sont correctes, et les stocke dans une base de données. Il expose une API pour les consulter.
3. **L'accès extérieur** : un utilisateur se connecte au serveur depuis l'extérieur (navigateur ou API) et voit l'état de la machine.

```
Machine surveillée        Serveur                          Utilisateur
┌─────────────┐  envoi   ┌──────────────────────┐  accès  ┌──────────────┐
│   Agent     │ ───────▶ │ API + Base de données│ ◀────── │ Navigateur   │
└─────────────┘  (HTTP)  └──────────────────────┘         │ ou API       │
                                                          └──────────────┘
```

## Données relevées

- Utilisation du processeur (CPU)
- Utilisation de la mémoire (RAM)
- Utilisation du disque
- Les 10 processus les plus gourmands (nom, PID, CPU, RAM)

