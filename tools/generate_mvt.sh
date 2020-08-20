#!/usr/bin/env bash
set -euo pipefail

# converts GeoJSON to MVT:
# ./generate_mvt.sh ./oa_gb_age_merged_constrained.geojson os_gb_age__mvt

if [ $# -ne 2 ]; then
  echo "Usage: `basename $0` SOURCE TARGET">&2 && exit;
fi

SOURCE=$1;
TARGET=$2;

if [ ! -f $SOURCE ]; then
  echo "'$SOURCE': no such file">&2 && exit;
fi

ARGS=(
    # automatically choose a maxzoom that should be sufficient to clearly distinguish the features and the detail within each feature
    "-zg"
    # if the tiles are too big at low zoom levels, drop the least-visible features to allow tiles to be created with those features that remain
    "--drop-densest-as-needed"
    # if even the tiles at high zoom levels are too big, keep adding zoom levels until one is reached that can represent all the features
    "--extend-zooms-if-still-dropping"
    # delete the mbtiles file if it already exists instead of giving an error
    "--force"
)

tippecanoe ${ARGS[@]} --output-to-directory=$TARGET $SOURCE
