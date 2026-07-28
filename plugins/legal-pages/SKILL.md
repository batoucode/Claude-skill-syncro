---
name: legal-pages
description: Génère automatiquement les pages légales (mentions légales, politique de confidentialité, CGV) conformes pour les sites web clients DesCodes.
---

# Pages Légales Obligatoires — DesCodes

Skill d'automatisation de la conformité juridique pour tous les sites web livrés aux clients DesCodes.

Cette skill s'active automatiquement à chaque création de site complet pour un client (artisan, TPE, association). Elle génère les trois pages légales obligatoires en France avec contenu préconfiguré, style cohérent et intégration au footer.

## Quand l'utiliser

Active cette skill dès qu'il est question de :
- **Créer** un site vitrine / site one-page / site multi-pages pour un client
- **Livrer ou déployer** un site complet pour un artisan, TPE ou association
- **Ajouter des pages** à un site client existant qui n'a pas encore ses pages légales

**Ne PAS l'activer pour** : CV, PDF, outils internes DesCodes/NEXUS, pages perso familiales, présentations, dashboards internes, maquettes.

## Comment l'utiliser

### Étape 1 : Collecte des informations

Avant de générer, j'ai besoin de ces informations (pour l'artisan/entreprise et l'hébergement) :

**Site**
- Nom du site
- URL (si connue, sinon placeholder)

**Artisan / Entreprise**
- Nom et prénom / raison sociale + forme juridique
- Adresse professionnelle complète
- Email de contact
- Téléphone
- SIRET (14 chiffres)
- Assujetti à la TVA ? (numéro de TVA intracommunautaire si oui)

**Hébergement**
- Nom de l'hébergeur (Vercel, OVH, o2switch, etc.)
- Adresse et téléphone de l'hébergeur

**Fonctionnalités du site**
- Le site permet-il la vente en ligne, la réservation payante, ou le paiement directement sur le site ?
  → Oui = générer les CGV  
  → Non = mentionner que CGV peuvent être ajoutées si besoin

### Étape 2 : Génération automatique

Je génère les fichiers HTML :
- `mentions-legales.html`
- `politique-confidentialite.html`
- `cgv.html` (uniquement si paiement en ligne)

Style cohérent avec la charte DesCodes actuelle (cyan `#00F2FF`, indigo `#7084FF`, orange `#F97316`, fonds clairs `#F6F5F2`, typos DM Sans/Ubuntu/JetBrains Mono).

### Étape 3 : Intégration

Je fournis :
- Les fichiers HTML à placer dans le projet
- Le code pour intégrer les liens dans le **footer** du site
- Lien crédit **DesCodes** systématique dans le footer

## Exemple d'usage

**Utilisateur :**
```
J'ai une nouvelle cliente, Céline Moreau, photographe (prestataire auto). 
Adresse : 42 rue des Acacia, 75014 Paris. 
Email : contact@celinemoreau.photo, Tel: 06 12 34 56 78
SIRET: 12345678901234
Elle n'a pas de TVA, le site c'est juste un portfolio + prise de contact.
URL: celinemoreau.photo
Hébergement: Vercel (défaut)
Active la skill legal-pages pour générer les pages
```

**Je fais :**
1. ✅ Valide les infos (SIRET, adresse, email)
2. ✅ Génère `mentions-legales.html`, `politique-confidentialite.html`
3. ✅ Fournis le code footer HTML avec les 3 liens + crédit DesCodes
4. ✅ Explique où placer les fichiers et comment intégrer les liens

---

## Règles de conformité

### Mentions Légales
- Éditeur (nom, statut EI/SARL/etc., adresse, SIRET, RNE, TVA)
- Directeur de la publication
- Hébergeur (nom, adresse, téléphone)

### Politique de Confidentialité (RGPD)
- Collecte (formulaire = nom, email, tél, message)
- Utilisation (gestion devis / relation commerciale)
- Conservation (3 ans max après dernier contact)
- Droits RGPD (accès, rectification, suppression) + réclamation CNIL

### CGV (si vente/paiement)
- Objet
- Prix, paiement, régime TVA
- Droit de rétractation (14 jours, sauf exécution commencée)
- Médiation consommation

---

## Structure des fichiers

```
project/
├── mentions-legales.html
├── politique-confidentialite.html
├── cgv.html (si applicable)
├── footer.html (ou intégrer les liens dans ton footer existant)
└── ...
```

## Footer — Lien crédit DesCodes

À ajouter systématiquement dans le footer (fond transparent, pas de couleur ajoutée) :

```html
<a href="https://descodes.com" target="_blank" rel="noopener noreferrer" 
   class="inline-flex items-center gap-1.5 font-inter text-[11px] text-zinc-400 hover:text-zinc-600 transition-colors tracking-wide">
  Site réalisé par<span class="font-bold">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512" 
         class="inline w-3.5 h-3.5 fill-[#F54927] mr-0.5" aria-hidden="true">
      <path d="M392.8 1.2c-17-4.9-34.7 5-39.6 22l-128 448c-4.9 17 5 34.7 22 39.6s34.7-5 39.6-22l128-448c4.9-17-5-34.7-22-39.6zm80.6 120.1c-12.5 12.5-12.5 32.8 0 45.3L562.7 256l-89.4 89.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l112-112c12.5-12.5 12.5-32.8 0-45.3l-112-112c-12.5-12.5-32.8-12.5-45.3 0zm-306.7 0c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3l112 112c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L77.3 256l89.4-89.4c12.5-12.5 12.5-32.8 0-45.3z"/>
    </svg>DES<span class="text-[#F54927]">CODES</span>
  </span>
</a>
```

---

**Pack DesCodes** : "Site clé en main + Conforme"  
Ne jamais livrer un site client sans ces pages légales ✅
