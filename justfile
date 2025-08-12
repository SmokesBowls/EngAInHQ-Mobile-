# Load .env automatically (we symlinked .env -> config/mobile.env)
set dotenv-load := true

# --- MrLore ---
lore topic:
    python3 clients/mrlore_bridge.py lore_query "{{topic}}"

# --- ClutterBot / Warroom ---
open path:
    python3 clients/clutter_bridge.py file_open "{{path}}"

diff path content:
    python3 clients/clutter_bridge.py diff_preview "{{path}}" "{{content}}"

stage path content:
    python3 clients/clutter_bridge.py file_save_staged "{{path}}" "{{content}}"

promote path:
    python3 clients/clutter_bridge.py promote_artifact "{{path}}"

# --- Health / Doctor ---
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
