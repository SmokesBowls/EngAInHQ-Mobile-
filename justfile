set dotenv-load := true

export CATHEDRAL_URL := \`grep CATHEDRAL_URL config/mobile.env | cut -d= -f2-\`
export MRLORE_URL    := \`grep MRLORE_URL config/mobile.env | cut -d= -f2-\`
export WARROOM_URL   := \`grep WARROOM_URL config/mobile.env | cut -d= -f2-\`
export AUTH_BEARER   := \`grep AUTH_BEARER config/mobile.env | cut -d= -f2-\`

lore topic:
    python3 clients/mrlore_bridge.py lore_query "{{topic}}"

# === Health ===
health:
    @echo "🔎 Running cathedral health checks..."
    python3 clients/health_check.py

doctor:
    @echo "📦 Env:"
    @echo "  CATHEDRAL_URL=${CATHEDRAL_URL}"
    @echo "  MRLORE_URL=${MRLORE_URL}"
    @echo "  WARROOM_URL=${WARROOM_URL}"
    @echo "  MODEL=${MODEL}"
    @echo
    just health

# === ClutterBot Commands ===
open path:
    python3 clients/clutter_bridge.py file_open "{{path}}"

diff path content:
    python3 clients/clutter_bridge.py diff_preview "{{path}}" "{{content}}"

promote path:
    python3 clients/clutter_bridge.py promote_artifact "{{path}}"

# === Health ===
health:
    @echo "🔎 Running cathedral health checks..."
    python3 clients/health_check.py

doctor:
    @echo "📦 Env:"
    @echo "  CATHEDRAL_URL=${CATHEDRAL_URL}"
    @echo "  MRLORE_URL=${MRLORE_URL}"
    @echo "  WARROOM_URL=${WARROOM_URL}"
    @echo "  MODEL=${MODEL}"
    @echo
    just health
