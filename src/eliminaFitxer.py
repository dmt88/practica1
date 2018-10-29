# -*- coding: utf-8 -*-
import os

# funci� que esborra el fitxer introdu�t per par�metre si existeix
def eliminaFitxer(nomFitxer):
    if os.path.exists(nomFitxer):
        try:
            os.remove(nomFitxer)
            print("Fitxer %s esborrat correctament." % nomFitxer)
        except OSError, e:
            print("Error: %s - %s." % (e.nomFitxer,e.strerror))
    else:
        print("No existeix el fitxer %s." % nomFitxer)
