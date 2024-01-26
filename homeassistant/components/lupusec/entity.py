"""Provides the Lupusec entity for Home Assistant."""
from homeassistant.helpers.entity import Entity

from .const import DOMAIN


class LupusecDevice(Entity):
    """Representation of a Lupusec device."""

    _attr_has_entity_name = True

    def __init__(self, data, device, config_entry) -> None:
        """Initialize a sensor for Lupusec device."""
        self._data = data
        self._device = device
        self._entry_id = config_entry.entry_id
        self._attr_unique_id = self.get_unique_id(
            config_entry.entry_id, device.device_id
        )

    def update(self):
        """Update automation state."""
        self._device.refresh()

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._device.name

    @property
    def device_info(self):
        """Return device information about the sensor."""
        return {
            "identifiers": {(DOMAIN, self._entry_id)},
            "name": f"Lupusec-XT{self._data.lupusec.model}",
            "manufacturer": "Lupus Electronics",
            "model": f"Lupusec-XT{self._data.lupusec.model}",
            "via_device": (DOMAIN, "lupusec_state"),
        }

    def get_unique_id(self, config_entry_id: str, key: str) -> str:
        """Create a unique_id id for a lupusec entity."""
        return f"{DOMAIN}_{config_entry_id}_{key}"
