#!/bin/bash
# Sıra dosyasındaki (render-queue.txt) bölümleri tek tek üretir; dosyaya yeni satır eklenebilir. Tek kopya çalışır.
Q="${1:-.cache/render-queue.txt}"; mkdir -p .cache; touch "$Q" "$Q.done"
while true; do
  E=$(grep -vxFf "$Q.done" "$Q" | head -1)
  if [ -z "$E" ]; then sleep 20; continue; fi
  while pgrep -f "check_and_render[.]sh" >/dev/null; do sleep 15; done
  tools/check_and_render.sh "$E"; echo "$E" >> "$Q.done"; echo "BİTTİ $E"
done
