# Meeting notes
**5.07.2022**
## Last week's progress
- Preprocessing almost finished
- two-lvel otsu finished
- two versions of two-level otsu
- Otsu and dice are vectorized --> reduced run time
- all gt images are reassigned to 0 and 1
- start to write report

## Questions
- Report: darf man HTML Befehle zur Formatierung verwenden? Bzw. wie kann man im Markdown Blocksatz einstellen (habe es bis jetzt nur mit einem HTML Befehl hinbekommen)

- WICHTIG: Warum funktioniert os.path.join nur auf windows und auf macOS nicht? (es liegt irgendwie am Einlesen der Bilder bzw. am Pathway). Kann man den code oder die pathways auf macOS irgendwie so anpassen oder umändern, dass os.path.join auch funktioniert und damit das Output auch das gleiche wie bei windows ist?
(in unserem Repository gibt es zum Veranschaulichen der unterschiedlichen Ergebnisse auch eine Version die auf macOS durchgelaufen ist und eine Version die auf windows durchgelaufen ist: macOS_preprocessing_short.ipynb und windows_preprocessing_short.ipynb)

- WICHTIG: Wie kann man über mehrere Ordner ein Package importieren? (wir haben z.b. alle Preprocessing Dateien in einem Preprocessing Ordner gesammelt. Dadurch funktioniert aber beim Ausführen der einzelnen Files das Importieren des Packages nicht mehr) 

- Wir haben in unserem Package eine Datei die __pycache_ heißt. Was ist das?
- Was sind .ipynb_checkpoints ? 

- Report: wir haben herausgefunden, dass die Reihenfolge bei Preprocessing auch entscheidend ist (also ob man zuerst stretching macht und dann filter oder umgekehrt). Sollen wir das auch im Report diskutieren? Sollen im Boxplot dann beide Varianten gezeigt werden oder reicht es wenn man nur die bessere Variante (also die mit höherem Dice score) zeigt

- Report: Frage über unsere beide Versionen von two-level otsu und local thresholding--> was in resport? Preprocessing immer für alle Datensätze machen? Oder kann man im Report auch nur einen bestimmten Datensatz aussuchen? (z. B. local thresholding --> nur NIH3T3 datensatz wegen variierendem Hintergrund; two-level otsu --> nur NIH3T3 wegen reflections... )

- Wir haben rausgefunden, dass between class otsu etwas schneller ist als Within class (Unterschied von 0,5-1s). Das ist jetzt nicht sehr signifikant und wir hatten alles davor auf within class variance. Sollen wir das dann anpassen oder reicht das, wenn wir das im Report diskutieren, da 1s wirklich nicht so sonderlich viel schneller ist. 

## Plans for next weeks
- 
