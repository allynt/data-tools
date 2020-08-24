# data-tools

A bunch of tools for working w/ data

## Usage

Typical usage is...

1. convert a Geometry Shapefile to GeoJSON: `python tools/convert_geometry.py --index "INDEX" --output data/geometry/processed/<filename>.geojson data/geometry/raw/oa/infuse_oa_lyr_2011_clipped.shp` where "INDEX" is the column to to identify each row (typically this is something like "OA code").
2. combine several Geometry GeoJSON files into a single Geometry GeoJSON file: `python tools/combine_geometry.py --ouput data/geometry/processed/<filename>.geojson data/geometry/processed/<file_1_to_merge>.geojson data/geometry/processed/<file_n_to_merge>.geojson`. This comes in handy when combining Scottish & English LSOA files.
3. merge a bunch of Data CSV files w/ the aforementioned Geometry files: `python tools/merge_data_and_geometry.py --geometry-index "index" --data-index "OA code" data/geometries/processed/oa_gb.geojson data/data/raw.isolation+/oa_gb_lfp_*.csv --output data/data/processed/oa_gb_lfp_merged.geojson` (note that --geometry-index is just set to "index" b/c it will have been renamed in step 1 above).
4. `python tools/constrain_data.pydata/metadata/columns_oa.json data/data/processed/oa_gb_lft_merged.geojson --output data/data/processed/oa_gb_lfp_merged_constrained.geojson`. "columns_oa.json" contains a dictionary mapping the column names of the CSV files to the names that ought to be displayed in **orbis**.
5. generate MVT from that converted/combined/merged/constrained data: `./tools/generate_mvt.sh data/data/processed/oa_gb_lfp_merged_constrained.geojson data/data/processed/oa_gb_lfp__mvt`
6. upload to **static-data-server**: `aws s3 cp --profile orbis-<environment> data/data/processed/oa_gb_lfp__mvt/ s3://astrosat-<environment>-staticdata/astrosat/isolation_plus/lfp/<version>/oa_gb_lfp__mvt/ --recursive`
7. ensure that the `DataSources` in **data-sources-directory** match the current state of the uploaded data.

In practice, steps 1-2 do not have to be redone. Steps 3-7 only have to be redone when the data-team changes the data. And Step 8 rarely has to be redone.

## notes

convention is to name files like: `<geometry>_<region>_<layer>_<processing>.geojson` where "geometry" is one of "oa", "lsoa", or "la", region is usually "gb", layer is one of the isolation_plus layers, and processing can be "merged" or "merged_constrained" or "\_\_mvt".

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
