# coding: utf-8
import unittest
import mimetypes
import Visionneuse

##
# Tests de verification du fonctionnement de la visionneuse
# Executer avec :
# python -m unittest testVisionneuse
#
class TestVisionneuse(unittest.TestCase):
    # def setUp(self):
    
    def test_EXERCICE_1_1_collecte(self):
        visi = Visionneuse.Visionneuse()
        listeDesFichiers = visi.collecte("./medias/sons")
        # Verification des resultats
        self.assertEqual(1, len(listeDesFichiers), "Le repertoire 'sons' doit contenir un fichier !")
        self.assertIn('./medias/sons/hibou.mp3', listeDesFichiers, "Le repertoire 'sons' doit contenir le fichier hibou.mp3 !")
        listeFichiers = visi.collecte("./medias")
        self.assertEqual(0, len(listeFichiers), "Le repertoire 'medias' ne contient que des repertoires !")
    
    
    def test_EXERCICE_1_2_collecteRecursive(self):
        visi = Visionneuse.Visionneuse()
        listeDesFichiers= visi.collecteRecursive("./medias")
        self.assertEqual(3, len(listeDesFichiers), "Le repertoire 'medias' doit contenir 3 fichiers !")
        self.assertIn('./medias/sons/hibou.mp3', listeDesFichiers, "Le repertoire 'sons' doit contenir le fichier hibou.mp3 !")
        self.assertIn('./medias/photos/raspberrypi.jpg', listeDesFichiers, "Le repertoire 'sons' doit contenir le fichier hibou.mp3 !")
        self.assertIn('./medias/videos/bbb_trailer_400p.ogv', listeDesFichiers, "Le repertoire 'sons' doit contenir le fichier hibou.mp3 !")
        
    def test_EXERCICE_2_1_obtientLeTypeMIME(self):
        visi = Visionneuse.Visionneuse()
        typeMimeDuFichierMp3 = visi.obtientLeTypeMIME('./medias/sons/hibou.mp3')
        self.assertEqual(typeMimeDuFichierMp3, mimetypes.types_map['.mp3'])
        typeMimeDuFichierJPG = visi.obtientLeTypeMIME('./medias/photos/raspberrypi.jpg')
        self.assertEqual(typeMimeDuFichierJPG, mimetypes.types_map['.jpg'])
        typeMimeDuFichierOGG = visi.obtientLeTypeMIME('./medias/videos/bbb_trailer_400p.ogv')
        self.assertEqual(typeMimeDuFichierOGG, mimetypes.types_map['.ogv'])
        
    def test_EXERCICE_2_2_obtientLesMetadonneesHachoir(self):
        visi = Visionneuse.Visionneuse()
        metadonneesHachoirDuFichierMp3 = visi.obtientLesMetadonneesHachoir('./medias/sons/hibou.mp3')
        self.assertIn('creation_date',metadonneesHachoirDuFichierMp3)
        self.assertEqual(metadonneesHachoirDuFichierMp3['endian'],"Big endian")
        metadonneesHachoirDuFichierJPG = visi.obtientLesMetadonneesHachoir('./medias/photos/raspberrypi.jpg')
        self.assertIn('compr_rate',metadonneesHachoirDuFichierJPG)
        self.assertEqual(metadonneesHachoirDuFichierJPG['width'],600, "L'image doit faire 600 pixels de large")
        metadonneesHachoirDuFichierOGG = visi.obtientLesMetadonneesHachoir('./medias/videos/bbb_trailer_400p.ogv')
        self.assertIn('duration',metadonneesHachoirDuFichierOGG)
        
    def test_EXERCICE_3_1_assemblageDesInfos(self):
        visi = Visionneuse.Visionneuse()
        listeDesFichiers= visi.collecteRecursive("./medias")
        tableDesInformations = visi.assemblageDesInfos(listeDesFichiers)
        self.assertIn('./medias/sons/hibou.mp3',tableDesInformations)
        informationsSurLeFichierMP3 = tableDesInformations['./medias/sons/hibou.mp3']
        self.assertIn('chemin_complet',informationsSurLeFichierMP3)
        self.assertEqual(informationsSurLeFichierMP3['type_mime'],"audio/mpeg")
        informationsSurLeFichierJPG = tableDesInformations['./medias/photos/raspberrypi.jpg']
        self.assertIn('chemin_complet',informationsSurLeFichierMP3)
        self.assertEqual(informationsSurLeFichierJPG['type_mime'],"image/jpeg")
        
    def test_EXERCICE_4_1_lectureDesFichiers(self):
        visi = Visionneuse.Visionneuse()
        listeDesFichiers= visi.collecteRecursive("./medias")
        tableDesFichiers = visi.assemblageDesInfos(listeDesFichiers)
        visi.lectureDesFichiers(tableDesFichiers)
        # La verification de ce test n'est pas automatisee, il faut
        # observer le resultat de l'execution a l'ecran
        
if __name__ == '__main__':
    unittest.main()
