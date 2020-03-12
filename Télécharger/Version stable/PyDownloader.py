# coding=utf-8
import wget
# import mkdir (non utilisé car solution pour télécharger dans le dossier 'Fichiers téléchargés' n'a pas encore été
# trouvé

print("Ce programme a été fabriqué dans l'IDE python PyCharm.")
# mkdir.mkdir('Fichiers téléchargés')
download_url = input("Entrez l'url du fichier à télécharger...")
name_of_file = input("Entrez le nom que vous voulez donner au fichier...")
filename = wget.download(download_url, name_of_file)
print("Votre fichier à été téléchargé !")
