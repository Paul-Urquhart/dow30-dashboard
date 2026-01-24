#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../.env"


curl --request GET "$HOST/api/2.0/fs/files/Volumes/dow30/default/export/gold_index.csv" \
  --header "Authorization: Bearer $TOKEN" \
  --output $FILE_PATH/gold_dow_index.csv

curl --request GET "$HOST/api/2.0/fs/files/Volumes/dow30/default/export/gold_top5.csv" \
  --header "Authorization: Bearer $TOKEN" \
  --output $FILE_PATH/gold_top5.csv

curl --request GET "$HOST/api/2.0/fs/files/Volumes/dow30/default/export/gold_bottom5.csv" \
  --header "Authorization: Bearer $TOKEN" \
  --output $FILE_PATH/gold_bottom5.csv
