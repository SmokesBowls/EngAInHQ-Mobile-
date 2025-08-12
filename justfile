set dotenv-load := true

export CATHEDRAL_URL := \`grep CATHEDRAL_URL config/mobile.env | cut -d= -f2-\`
export MRLORE_URL    := \`grep MRLORE_URL config/mobile.env | cut -d= -f2-\`
export WARROOM_URL   := \`grep WARROOM_URL config/mobile.env | cut -d= -f2-\`
export AUTH_BEARER   := \`grep AUTH_BEARER config/mobile.env | cut -d= -f2-\`

lore topic:
    python3 clients/mrlore_bridge.py lore_query "{{topic}}"
