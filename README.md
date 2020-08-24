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
7. upload to **static-data-server**: `aws s3 cp --profile orbis-<environment> ./<whatever> s3://astrosat-<environment>-staticdata/<whatever> --recursive`

## notes

"./data" points to:

```
.
├── data
│   ├── processed
│   │   ├── geometry_region_layer_merged_constrained.geojson
│   │   ├── geometry_region_layer_merged.geojson
│   │   └── geometry_region_layer__mvt
│   │       └── z
│   │           └── x
│   │               └── y.pbf
│   └── raw
│       └── soft link to CSV files processed by the data-team
├── geometry
│   ├── processed
│   │   ├── lad_gb.geojson
│   │   ├── lsoa_england_wales.geojson
│   │   ├── lsoa_gb.geojson
│   │   ├── lsoa_scotland.geojson
│   │   └── oa_gb.geojson
│   └── raw
│       ├── lad
│       │   └── <shapefiles>
│       ├── lsoa
│       │   └── <shapefiles>
│       └── oa
│       └── oa
│           └── <shapefiles>
├── metadata
│   ├── columns_lad.json
│   ├── columns_lsoa.json
│   └── columns_oa.json
└── README
```
