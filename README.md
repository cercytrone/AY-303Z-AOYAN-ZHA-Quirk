## Eigene / Benutzerdefinierte Quirks einbinden

[AY-303Z-AOYAN - ZigBee Soil Moisture Tester - Aliexpress -](https://aliexpress.com/item/1005012719571932.html) 

Wenn ein Gerät nicht korrekt erkannt wird und du einen angepassten Quirk nutzt (z. B. eine .py-Datei für ein Tuya-Gerät):
1. Ordner erstellen: Erstelle im Hauptverzeichnis deines Home Assistant (dort, wo die configuration.yaml liegt) einen Ordner namens zha_quirks (oder /config/custom_zha_quirks).
2. Pfad hinterlegen: Füge in deiner configuration.yaml den Pfad hinzu:
```  
yaml

zha:
  custom_quirks_path: /config/custom_zha_quirks'
```  

3. Datei hochladen: Lade die entsprechende Python-Quirk-Datei (z. B. via File Editor oder Studio Code Server) in diesen Ordner, oder via Terminal "nano /config/custom_zha_quirks/aoyan_ay303z.py" und den Inhalt einfügen.
4. Neustart & Neu koppeln:
	• Starte Home Assistant vollständig neu.
	• Lösche das betreffende Zigbee-Gerät in ZHA und kopple es danach neu, damit der Quirk beim Einlesen der Signatur greift.
