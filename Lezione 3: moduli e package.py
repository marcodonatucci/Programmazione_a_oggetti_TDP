# La funzione import crea un namespace e lo popola con le definizioni che ho scritto nel modulo importato
# un modulo è un insieme di classi, funzioni, variabili, dichiarazioni...
# Un file .py che contiene solo definizioni e non ha un main è un modulo, puoi importarlo nel programma che stai creando
# il nome del modulo è uguale al nome del file, import cerca il file, lo esegue, e mette i dati in un namespace nuovo
# import nomeModulo as rinomina, cambia il nome per rendertela più semplice
# import nomeFunzione from nomeModulo, importa l'oggetto che ti serve dal modulo
# quando definisci un modulo è utile scrivere qualche riga di test per i metodi direttamente in locale nel modulo
# per lanciare il codice solo nel modulo stesso in cui è scritto per testarlo e non quando viene importato:
# if __name__ == "__main__":, name è il parametro che mi dice il nome del modulo
# all'interno del modulo stesso name si chiama main e non con il nome del modulo
# i nomi che iniziano con _ non vengono importati! Utile per i test
# le cartelle del progetto sono i package (puoi avere subpackage), per importare moduli di altri package:
# import nomePackage.nomeModulo
# il file __init__.py dice a python che quella cartella è un package, viene eseguito all'inizio di import
# puoi installare e importare (solo dopo aver installato...) moduli esterni da pypi.org
# (python installs programs) pip projectName, è il comando da usare per installare moduli esterni
# puoi usare l'icona a panino a sinistra su pycharm anche per installare
# puoi installare moduli esterni localmente in un progetto e non globalmente sul pc usando il venv (virtual environment)
# quando stai lavorando su un venv in basso a destra vedi la versione di python e tra parentesi il nome del modulo venv
# se non lo stai usando puoi premere sulla versione e aggiungere un venv locale
# crea un file requirements.txt in cui c'è l'elenco dei moduli importati nel progetto (pycharm ti aiuta a farlo)
