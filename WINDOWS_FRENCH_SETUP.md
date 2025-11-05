# 🪟 Guide d'installation Windows (Français)

## ❌ Erreur: "Le chemin d'accès spécifié est introuvable"

Cette erreur signifie que l'environnement virtuel n'existe pas encore.

## ✅ Solution: Exécutez setup.bat d'abord!

### Étape 1: Ouvrez l'Invite de commandes

1. Appuyez sur `Win + R`
2. Tapez `cmd`
3. Appuyez sur Entrée

### Étape 2: Naviguez vers le dossier du projet

```batch
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904
```

### Étape 3: Exécutez le script d'installation

```batch
setup.bat
```

**Attendez 2-3 minutes** pendant que:
- L'environnement virtuel est créé
- Les packages Python sont installés
- Le navigateur Chrome est téléchargé

Vous verrez: `✅ Setup complete!`

### Étape 4: Maintenant activez l'environnement

```batch
venv\Scripts\activate.bat
```

Vous verrez `(venv)` au début de votre ligne de commande.

### Étape 5: Testez la génération de vidéo

```batch
python bot.py --mode test
```

## 🎯 Ordre correct des commandes:

```batch
REM 1. Aller au dossier du projet
cd C:\Users\smart\OneDrive\Desktop\Cursor-cursor-automated-asmr-video-generation-and-tiktok-posting-b904

REM 2. Installation (première fois seulement)
setup.bat

REM 3. Activer l'environnement
venv\Scripts\activate.bat

REM 4. Tester
python bot.py --mode test

REM 5. Poster une fois
python bot.py --mode once

REM 6. Mode automatique
start_bot.bat
```

## ⚠️ Si setup.bat ne fonctionne pas:

### Vérifier Python:

```batch
python --version
```

Vous devriez voir: `Python 3.8.x` ou supérieur

**Si Python n'est pas installé:**
1. Téléchargez: https://www.python.org/downloads/
2. Installez avec "Add to PATH" coché
3. Redémarrez l'Invite de commandes

### Installation manuelle:

```batch
REM Créer l'environnement virtuel
python -m venv venv

REM Activer
venv\Scripts\activate.bat

REM Installer les dépendances
pip install --upgrade pip
pip install -r requirements.txt

REM Installer le navigateur
playwright install chromium

REM Créer le fichier .env
copy .env.example .env
```

## 📞 Besoin d'aide?

Ouvrez `WINDOWS_SETUP.md` pour le guide complet en anglais.
