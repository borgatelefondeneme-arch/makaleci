#!/usr/bin/env bash
# Yerel Türkçe seslendirme (Piper) kurulumu. ElevenLabs anahtarı yokken kullanılır.
# DİKKAT: tr_TR-dfki sesinin eğitim verisi CC BY-NC-SA 4.0 lisanslıdır (ticari kullanım dışı);
# gelir getiren yayınlar için ElevenLabs ya da ticari kullanıma açık bir ses gerekir.
set -euo pipefail
VOICE="${1:-tr_TR-dfki-medium}"
DIR=".cache/piper"
mkdir -p "$DIR"
python3 -c "import piper" 2>/dev/null || pip install piper-tts
IFS=- read -r lang name quality <<<"$VOICE"
for f in "$VOICE.onnx" "$VOICE.onnx.json"; do
  [ -f "$DIR/$f" ] || curl -fL -o "$DIR/$f" "https://huggingface.co/rhasspy/piper-voices/resolve/main/${lang%_*}/$lang/$name/$quality/$f"
done
echo "hazır: $DIR/$VOICE.onnx"
