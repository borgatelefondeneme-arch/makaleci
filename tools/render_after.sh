#!/bin/bash
# Çalışan render kuyruğu bitince verilen bölümleri sırayla üretir.
while pgrep -f "render_queue[.]sh" >/dev/null; do sleep 30; done
for E in "$@"; do tools/check_and_render.sh "$E"; echo "BİTTİ $E"; done
