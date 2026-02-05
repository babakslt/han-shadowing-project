#!/usr/bin/env bash
set -euo pipefail

#mkdir -p vendor

#curl -L -o vendor/react.production.min.js https://unpkg.com/react@18/umd/react.production.min.js
#curl -L -o vendor/react-dom.production.min.js https://unpkg.com/react-dom@18/umd/react-dom.production.min.js
#curl -L -o vendor/babel.min.js https://unpkg.com/@babel/standalone/babel.min.js
#curl -L -o vendor/tailwindcss.min.js https://cdn.tailwindcss.com
curl -L -o vendor/md5.min.js https://cdnjs.cloudflare.com/ajax/libs/blueimp-md5/2.19.0/js/md5.min.js
curl -L -o vendor/js-yaml.min.js https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js
curl -L -o vendor/pinyin-pro.min.js https://unpkg.com/pinyin-pro@3.18.2/dist/index.js

ls -lh vendor
