#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../.env"


aws s3 sync \
    s3://paul-dow30-data/export/dow_prod/ \
    $FILE_PATH