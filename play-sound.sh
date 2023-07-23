#!/bin/bash

# Setup venv

MYCROFT_CONF=/etc/mycroft/mycroft.conf
VENV_CMD=
if [[ -f "$MYCROFT_CONF" ]] && grep -q '"platform":.*"mycroft_mark_1"' $MYCROFT_CONF; then
    VENV_CMD=". /opt/venvs/mycroft-core/bin/activate;"
fi

# Execute the script.
exec /bin/bash -c "$VENV_CMD mplayer -volume 175 \"/opt/mycroft/skills/record-that-skill/xbox-sound.mp3\" > /dev/null 2>&1"
