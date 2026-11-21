# AOYAN AY-303Z – ZHA Custom Quirk

[AY-303Z-AOYAN - ZigBee Soil Moisture Tester - Aliexpress -](https://aliexpress.com/item/1005012719571932.html) 

## English

1. **Create a folder:** In the Home Assistant configuration directory, create a folder for custom quirks, e.g. `/config/custom_zha_quirks/`.
2. **Save the quirk:** Put the quirk into that folder as a `.py` file, e.g. `aoyan_ay303z.py`. Keep only one file for this device there.
3. **Set the path:** Add this to `configuration.yaml`, using the exact folder name from step 1:

   ```yaml
   zha:
     custom_quirks_path: /config/custom_zha_quirks/
   ```

4. **Restart:** Fully restart Home Assistant.
5. **Pair the device:** Remove the sensor from ZHA and pair it again so the entities are created to match the quirk.
6. **Verify:** The device page should show temperature, soil moisture and battery. Values arrive within a few minutes after pairing.

After later changes to the quirk, a restart is enough. Re-pairing is only needed when entities are added or removed.


## Deutsch

1. **Ordner anlegen:** Im Konfigurationsordner von Home Assistant einen Ordner für eigene Quirks erstellen, z. B. `/config/custom_zha_quirks/`.
2. **Quirk speichern:** Den Quirk als `.py`-Datei in diesen Ordner legen, z. B. `aoyan_ay303z.py`. Es darf nur eine Datei für dieses Gerät dort liegen.
3. **Pfad eintragen:** In der `configuration.yaml` ergänzen, mit exakt dem Ordnernamen aus Schritt 1:

   ```yaml
   zha:
     custom_quirks_path: /config/custom_zha_quirks/
   ```

4. **Neu starten:** Home Assistant komplett neu starten.
5. **Gerät anlernen:** Den Sensor in ZHA entfernen und neu anlernen, damit die Entitäten passend zum Quirk angelegt werden.
6. **Prüfen:** Auf der Geräteseite sollten Temperatur, Bodenfeuchte und Batterie erscheinen. Die Werte kommen innerhalb weniger Minuten nach dem Anlernen.

Bei späteren Änderungen am Quirk genügt ein Neustart. Neu anlernen ist nur nötig, wenn Entitäten hinzukommen oder wegfallen.
