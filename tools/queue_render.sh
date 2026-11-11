#!/bin/bash
# Başka bir render sürüyorsa bitmesini bekler, sonra bölümü kontrol karesi + video olarak üretir.
E="$1"; sleep $((RANDOM % 5))
while pgrep -f "check_and_render.sh" | grep -v $$ >/dev/null 2>&1 && [ "$(pgrep -f 'pipeline/render/(cli|frames).ts' | wc -l)" -gt 0 ]; do sleep 20; done
exec tools/check_and_render.sh "$E"
