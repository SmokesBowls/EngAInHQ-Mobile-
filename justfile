
doctor:
    @echo "📦 Env:"
    @echo "  CATHEDRAL_URL=${CATHEDRAL_URL}"
    @echo "  MRLORE_URL=${MRLORE_URL}"
    @echo "  WARROOM_URL=${WARROOM_URL}"
    @echo "  MODEL=${MODEL}"
    @echo
    just health
