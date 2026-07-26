# Claude Skill Syncro 🚀

Synchronisation personnelle des skills Claude Code entre plusieurs PC via GitHub.

## 🎯 Objectif

Ce repo centralise tes skills Claude Code personnalisées pour que tu puisses les utiliser sur **tous tes PC** avec le même compte Claude Code. Les skills se synchronisent automatiquement via Git.

## 🏗️ Structure

```
Claude-skill-syncro/
├── .claude-plugin/
│   └── marketplace.json          # Catalogue des skills
├── plugins/
│   ├── ui-ux-pro-max/
│   │   ├── SKILL.md             # Fichier de la skill
│   │   └── data/                # Données/ressources (optionnel)
│   └── [autres-skills]/
├── README.md                     # Ce fichier
└── .gitignore
```

## 📖 Comment ça marche

### Le système de marketplace Claude Code

1. **Marketplace** = un repo Git contenant un `marketplace.json`
2. **Plugin** = une skill empaquetée avec ses données et scripts
3. **Installation** = une commande Claude Code qui enregistre la marketplace et installe les skills

Quand tu mets à jour une skill et que tu pusses sur GitHub, les autres PC peuvent récupérer les changements en une commande.

## 🚀 Installation sur un nouveau PC

### Première utilisation

```bash
# Ouvre Claude Code dans un terminal
claude

# À l'intérieur de Claude Code, enregistre le marketplace
/plugin marketplace add batoucode/Claude-skill-syncro

# Installe une skill (ex: ui-ux-pro-max)
/plugin install ui-ux-pro-max@Claude-skill-syncro

# Recharge les plugins pour qu'ils soient actifs
/reload-plugins
```

### Mise à jour des skills

Quand tu mets à jour une skill sur GitHub, les autres PC récupèrent la version à jour :

```bash
# Rafraîchis le catalogue du marketplace
/plugin marketplace update Claude-skill-syncro

# Recharge les plugins actifs
/reload-plugins
```

## 📚 Utilisation des skills

Une fois installée, une skill est disponible comme :
- **Commandes slash** : `/ma-skill-commande`
- **Agents** : agents Claude Code spécialisés
- **Hooks** : exécution automatique dans certains contextes

Pour voir les skills installées et actives :

```
/plugin list
```

## ➕ Ajouter une nouvelle skill

### Étape 1 : Créer le dossier

```bash
mkdir -p plugins/ma-nouvelle-skill
```

### Étape 2 : Créer le SKILL.md

Chaque skill nécessite un fichier `SKILL.md` avec ce format minimal :

```markdown
---
name: ma-nouvelle-skill
description: Description brève de ce que fait cette skill
---

# Ma Nouvelle Skill

Description longue...

## Quand l'utiliser

Explique dans quels cas tu vas utiliser cette skill.

## Comment l'utiliser

Explique comment l'invoquer et quels paramètres elle accepte.

## Exemple

Montre un exemple concret d'usage.
```

Voir `plugins/ui-ux-pro-max/SKILL.md` pour un exemple complet.

### Étape 3 : Ajouter la skill au marketplace.json

Dans `.claude-plugin/marketplace.json`, ajoute un objet à la liste `plugins` :

```json
{
  "id": "ma-nouvelle-skill",
  "name": "Ma Nouvelle Skill",
  "version": "1.0.0",
  "description": "Description brève",
  "author": "batoucode",
  "tags": ["tag1", "tag2"]
}
```

### Étape 4 : Commiter et pusher

```bash
git add .
git commit -m "feat: add ma-nouvelle-skill"
git push
```

## 🔐 Gestion des credentials

Les skills peuvent avoir besoin de tokens d'authentification (GitHub, API keys, etc.). **Ne commite jamais de secrets dans ce repo.**

### Solution recommandée

Stocke les credentials dans **Google Drive** (fichier `claude-config`), et :
- Référence-les dans la skill par chemin
- Ou charge-les depuis une variable d'environnement
- Ou utilise des `~/.env` locaux (non committé via `.gitignore`)

**Exemple dans une skill** :
```markdown
# Credentials

Le fichier `~/.claude-credentials/github-token` doit contenir ton token GitHub.

```bash
mkdir -p ~/.claude-credentials
echo "ghp_xxxxx" > ~/.claude-credentials/github-token
chmod 600 ~/.claude-credentials/github-token
```
```

## 🔄 Flux de travail multi-PC

### Scénario : créer un projet sur PC1 et le finir sur PC2

**Sur PC1 :**
1. Pull la dernière version des skills : `/plugin marketplace update Claude-skill-syncro`
2. Lance une skill qui crée un projet GitHub (ex: `vercel-deploy`)
3. Le projet est créé sur GitHub

**Sur PC2 :**
1. Pull la dernière version des skills : `/plugin marketplace update Claude-skill-syncro`
2. Clone le projet créé : `git clone https://github.com/batoucode/mon-projet`
3. Continue le travail
4. Push tes changements

Les changements se synchro automatiquement via GitHub. Si tu mises à jour une **skill** :

1. Commite et pousse sur `Claude-skill-syncro`
2. Sur chaque PC : `/plugin marketplace update Claude-skill-syncro` + `/reload-plugins`

## 📋 Checklist avant de livrer une skill

- [ ] `SKILL.md` complète avec description claire
- [ ] Sections "Quand l'utiliser" et "Comment l'utiliser" présentes
- [ ] Exemple d'usage fourni
- [ ] Pas de credentials en dur (utilise `~/.env` ou Google Drive)
- [ ] Tags appropriés dans `marketplace.json`
- [ ] Version mise à jour (format sémantique : 1.0.0)
- [ ] Tests locaux validés sur PC actuel
- [ ] Commit message clair

## 🛠️ Dépannage

### "Marketplace not found" / "Plugin not installed"

```bash
# Rafraîchis le catalogue
/plugin marketplace update Claude-skill-syncro

# Vérifie que la marketplace est enregistrée
/plugin marketplace list
```

### La skill n'est pas active

```bash
# Recharge les plugins
/reload-plugins

# Vérifie l'état
/plugin list
```

### Les changements ne s'appliquent pas

1. Vérifie que tu as pushé sur GitHub
2. Fais `/plugin marketplace update Claude-skill-syncro`
3. Fais `/reload-plugins`
4. Redémarre Claude Code si ça persiste

### Une skill dépend d'un fichier manquant

Assure-toi que le fichier :
- Est dans le dossier `plugins/ma-skill/`
- A été commité et pushé
- Est correct après `git pull`

## 📊 Statistiques

- **Nombre de skills** : à jour dans le marketplace.json
- **Taille du repo** : ~50 MB (skills = texte pur, très léger)
- **Temps de sync** : < 1 seconde (git clone/pull)

## 🔗 Liens utiles

- [Documentation Claude Code](https://code.claude.com/docs/)
- [Plugin Marketplace Guide](https://code.claude.com/docs/en/discover-plugins)
- [Créer une skill Claude Code](https://code.claude.com/docs/en/building-skills)

## 📝 Historique des changements

### v1.0.0 (2026-07-26)
- Initialisation du repo
- Première skill : `ui-ux-pro-max`

---

**Maintenu par** : batoucode  
**Dernier update** : 2026-07-26
