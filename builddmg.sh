#!/bin/sh

create-dmg \
  --volname "Simple Labels for vMix" \
  --volicon "SL_logo_diskimege_SL_vMix.icns" \
  --background "pic.png" \
  --eula "EULA.txt" \
  --add-file "README.txt" "README.md" 500 150 \
  --add-file "EULA.txt" "EULA.txt" 630 150 \
  --window-pos 200 200 \
  --text-size 15 \
  --window-size 720 360 \
  --icon-size 120 \
  --icon "Simple Labels for vMix.app" 110 150 \
  --hide-extension "Simple Labels for vMix.app" \
  --app-drop-link 270 150 \
  --no-internet-enable \
  "dist/Simple Labels for vMix.dmg" \
  "dist/dmg/"