# /bin/bash
set -e

docker-compose up -d

newman run ./e2e-tests/e2e-2xx-4xx-music-metadata.postman_collection.json

docker stop mongo

newman run ./e2e-tests/e2e-5xx-music-metadata.postman_collection.json

docker-compose down
