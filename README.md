# data-tools

A bunch of tools for working w/ data

## Usage

Typical usage is...

1. get original shapefile for geometry
2. `convert_geometry` to convert shapefile to geojson
3. `combine_geometry` to combine a bunch of geometry geojson files (to combine scottish & english geometry for instance)
4. `merge_data_and_geometry` to merge a bunch of data CSV files w/ the aforementioned geometry
5. `constrain_data` to select a subset of data columns (and potentially rename them)
6. `generate_mvt` to convert that converted/combined/merged/constrained data from GeoJSON to MVT
