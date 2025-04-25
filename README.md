```markdown
# Touillette CTF Challenge

## Description

“Touillage” est une obfuscation en deux étapes d’un flag de 64 caractères. On transpose d’abord les octets via une matrice 8×8 en lisant chaque colonne de bas en haut, puis on mélange indices impairs et pairs.

## Fichiers

- **output.txt** : le flag « touillé » (chiffré), 64 caractères
- **touilette.py** : script Python qui décrypt flag original
- **reverse_touilette.py** : script Python qui récupère le flag original


## Usage

1. Cloner ou télécharger ce dépôt.
2. Placer le flag chiffré dans `output.txt` (une ligne, 64 caractères).
3. Lancer :
   ```bash
   python decrypt.py output.txt
   ```
4. Le script affiche le flag original :
   ```
   FCSC{...}
   ```

## Principe

1. **Transposition colonne inversée**  
   ```python
   x = "".join([
       flag[-8::-8],  # indices 56,48,…,0
       flag[-7::-8],  # indices 57,49,…,1
       …
       flag[-1::-8],  # indices 63,55,…,7
   ])
   ```
   On imagine le flag en matrice 8×8 (ligne par ligne), puis on lit colonne par colonne de bas en haut.

2. **Mélange impairs/pairs**  
   ```python
   y = x[1::2] + x[0::2]
   ```
   On concatène d’abord les indices impairs de `x`, puis les indices pairs.

## Licence

Projet sous licence MIT.
```

