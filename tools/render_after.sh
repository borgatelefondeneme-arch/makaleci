#!/bin/bash
# Çalışan render bitince verilen bölümleri sırayla üretir.
while pgrep -f "render_queue[.]sh|check_and_render[.]sh" >/dev/null; do sleep 20; done
for E in "$@"; do tools/check_and_render.sh "$E"; echo "BİTTİ $E"; done
