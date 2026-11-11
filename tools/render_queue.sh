#!/bin/bash
# Verilen bölümleri sırayla üretir; çalışan başka bir render varsa önce onun bitmesini bekler.
while pgrep -f "check_and_render.sh" >/dev/null; do sleep 20; done
for E in "$@"; do tools/check_and_render.sh "$E"; echo "BİTTİ $E"; done
