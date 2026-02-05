This folder can hold locally cached browser libraries to speed up loading.

Run `bash scripts/fetch-vendor.sh` to download:
- react.production.min.js
- react-dom.production.min.js
- babel.min.js
- tailwindcss.min.js
- md5.min.js
- js-yaml.min.js
- pinyin-pro.min.js

If files are missing, the app will automatically fall back to CDN URLs.
