#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../.env"


aws s3 cp \
    s3://paul-dow30-data/export/dow_prod/gold_dow_index.csv \
    $FILE_PATH/gold_dow_index.csv

aws s3 cp \
    s3://paul-dow30-data/export/dow_prod/gold_top5.csv \
    $FILE_PATH/gold_top5.csv

aws s3 cp \
    s3://paul-dow30-data/export/dow_prod/gold_bottom5.csv \
    $FILE_PATH/gold_bottom5.csv