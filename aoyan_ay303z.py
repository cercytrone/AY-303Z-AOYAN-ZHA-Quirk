import zigpy.types as t
from zigpy.quirks.v2 import EntityType
from zigpy.quirks.v2.homeassistant import PERCENTAGE, UnitOfTemperature, UnitOfTime
from zigpy.zcl.clusters.measurement import RelativeHumidity

from zhaquirks.tuya.builder import TuyaQuirkBuilder


class TemperatureUnit(t.enum8):
    Celsius = 0x00
    Fahrenheit = 0x01


(
    TuyaQuirkBuilder("AOYAN", "AY-303Z")
    .applies_to("AOYAN  ", "AY-303Z")
    .removes(RelativeHumidity.cluster_id)     # Gerät hat keinen Luftfeuchte-Sensor
    # Messwerte
    .tuya_temperature(dp_id=5, scale=10)      # 229 -> 22,9 °C
    .tuya_soil_moisture(dp_id=3)              # Bodenfeuchte % (DP 109 meldet denselben Wert)
    .tuya_battery(dp_id=15)                   # Batterie %
    # Einstellungen
    .tuya_enum(
        dp_id=9,
        attribute_name="temperature_unit",
        enum_class=TemperatureUnit,
        entity_type=EntityType.CONFIG,
        translation_key="temperature_unit",
        fallback_name="Temperatureinheit",
    )
    .tuya_number(
        dp_id=102,
        attribute_name="soil_calibration",
        type=t.int32s,
        min_value=-30,
        max_value=30,
        step=1,
        unit=PERCENTAGE,
        entity_type=EntityType.CONFIG,
        translation_key="soil_calibration",
        fallback_name="Kalibrierung Bodenfeuchte",
    )
    .tuya_number(
        dp_id=104,
        attribute_name="temperature_calibration",
        type=t.int32s,
        min_value=-2,
        max_value=2,
        step=0.1,
        multiplier=0.1,
        unit=UnitOfTemperature.CELSIUS,
        entity_type=EntityType.CONFIG,
        translation_key="temperature_calibration",
        fallback_name="Kalibrierung Temperatur",
    )
    .tuya_number(
        dp_id=110,
        attribute_name="soil_warning_threshold",
        type=t.uint32_t,
        min_value=0,
        max_value=100,
        step=1,
        unit=PERCENTAGE,
        entity_type=EntityType.CONFIG,
        translation_key="soil_warning_threshold",
        fallback_name="Schwellwert Trockenheitswarnung",
    )
    .tuya_number(
        dp_id=111,
        attribute_name="temperature_sampling",
        type=t.uint32_t,
        min_value=5,
        max_value=3600,
        step=1,
        unit=UnitOfTime.SECONDS,
        entity_type=EntityType.CONFIG,
        translation_key="temperature_sampling",
        fallback_name="Messintervall Temperatur",
    )
    .tuya_number(
        dp_id=112,
        attribute_name="soil_sampling",
        type=t.uint32_t,
        min_value=5,
        max_value=3600,
        step=1,
        unit=UnitOfTime.SECONDS,
        entity_type=EntityType.CONFIG,
        translation_key="soil_sampling",
        fallback_name="Messintervall Bodenfeuchte",
    )
    .skip_configuration()
    .add_to_registry()
)