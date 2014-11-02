# coding: utf-8
import logging

#
logger = logging.getLogger('visionneuse')
logger.addHandler(logging.StreamHandler())
####
        
class Visionneuse:
    tableDesFichiers = {}
        
    ##
    # EXERCICE 1.1:
    # Cette fonction inspecte le chemin en argument et retourne une liste de fichiers correspondants.
    # Les fichiers sont identifiés avec un chemin relatif à la visionneuse.
    # Attention, la fonction ne doit pas retourner de dossiers, seulement des fichiers.
    def collecte(self,chemin): 
        logger.debug("Collecte des fichiers dans le dossier "+chemin)
        return []
        
    ##
    # EXERCICE 1.2:
    # Cette fonction inspecte le dossier "chemin" et trouve les fichiers présents dans la hiérarchie complète.
    # Elle appelle la fonction "collecte()" pour chaque dossier qu'elle trouve
    # dans le chemin donné de manière récursive.
    #
    def collecteRecursive(self,chemin):
        logger.debug("Collecte recursive des fichiers dans le dossier "+chemin)
        return []
        
    ##
    # EXERCICE 2.1:
    # Pour le fichier donné, retourne le type MIME
    # Note : vous pouvez utiliser Hachoir ou la bibliotheque systeme "mimetypes"
    # Attention, nous voulons seulement le type MIME, pas l'encodage
    def obtientLeTypeMIME(self,fichier):
        logger.debug("Obtention du type MIME pour "+fichier)
        return ""
          
    ##
    # EXERCICE 2.2:
    # Pour le fichier donné, retourne les metadonnées Hachoir.
    # Il faut retourner les donnees dans une tables associative,
    # qui associe le nom de l'attribut Hachoir avec sa valeur.
    # Par exemple :
    #    resultat['comment'] =  "Taken from my Android Phone on 15 Oct 2014"
    #    resultat['width'] =  480
    def obtientLesMetadonneesHachoir(self,fichier):
        logger.debug("Obtention des metadonnees pour "+fichier)
        resultat = {}
        return resultat
        
    ##
    # EXERCICE 3.1:
    # En utilisant les fonctions precedentes, assembler une table associative
    # qui associe le nom d'un fichier avec toutes les donnees disponibles a son
    # sujet, dont :
    #   * Le chemin complet (chemin + nom de fichier) du fichier ("chemin_complet")
    #   * Le type MIME du fichier ("type_mime")
    #   * Les metadonnees multimedia du fichier, prefixees avec "hachoir." ("hachoir.width")    
    def assemblageDesInfos(self,listeDeFichiers):
        logger.debug("Assemblage des informations pour "+`len(listeDeFichiers)`+" fichier(s)")
        return []
                
    ##
    # EXERCICE 4.1:
    # Pour chaque fichier dans la table, invoquer un programme
    # capable de lire le fichier en mode plein ecran, en fonction
    # du type MIME.
    # On utilise VLC pour les MP3 et les OGV, et gpicview pour les JPG/PNG
    def lectureDesFichiers(self,tableDesFichiers):
        logger.debug("Lecture des fichiers en sequence")
        
    ##
    # Cette methode utilise les exercices precedents, pour lancer la lecture
    def scanneLeRepertoire(self,chemin):
       logger.debug("Inspection du repertoire "+chemin)
       self.listeDesFichiers = self.collecteRecursive(chemin)
       self.tableDesFichiers = self.assemblageDesInfos(self.listeDesFichiers)
 
 
    ##
    # Constructeur de la classe Visionneuse
    # Initialize le logging
    def __init__(self):
        logger.setLevel(logging.DEBUG)
        logger.debug("Demarrage de la visionneuse")
        
        