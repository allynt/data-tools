import json

import pandas as pd
import geopandas as gpd


CRS = "EPSG:4326"


def clean_data_frame(data_frame):
    # replace NaN w/ None...
    data_frame = data_frame.where((pd.notnull(data_frame)), None)
    # check for duplicates...
    assert not any(data_frame.index.duplicated()), "duplicated rows"
    return data_frame


def combine_data_frames(left, right):
    assert left.index.name is not None and left.index.name == right.index.name
    df = right.combine_first(left)
    df = df.where((pd.notnull(df)), None)
    return df


def reindex_data_frame(data_frame, index_name="index"):
    assert index_name in data_frame.columns, f"index {index_name} not found; valid choices are: {', '.join(data_frame.columns)}."
    if index_name != "index":
        data_frame["index"] = data_frame[index_name]
    data_frame = data_frame.set_index("index")
    return data_frame


def select_and_rename_columns(data_frame, columns, ignore_missing=False):
    if ignore_missing:
        columns = {
            k: v for k, v in columns.items()
            if k in data_frame.columns
        }
    data_frame = data_frame[list(columns.keys())]
    data_frame = data_frame.rename(columns=columns)
    return data_frame


def import_geometry(geometry_file, index_name="index"):
    geo_data_frame = gpd.read_file(geometry_file)
    geo_data_frame = reindex_data_frame(geo_data_frame, index_name=index_name)
    geo_data_frame = clean_data_frame(geo_data_frame)
    return geo_data_frame


def import_really_big_geometry(geometry_file, index_name="index"):
    # working w/ OA is a PITA b/c it's really big;
    # I have to buffer the content in JSON or I run out of memory
    geo_data_content = json.load(geometry_file)
    geo_data_frame = gpd.GeoDataFrame.from_features(geo_data_content["features"])
    geo_data_frame = reindex_data_frame(geo_data_frame, index_name=index_name)
    geo_data_frame = clean_data_frame(geo_data_frame)
    return geo_data_frame


def import_data(data_file, index_name="index"):
    data_frame = pd.read_csv(data_file)
    data_frame = reindex_data_frame(data_frame, index_name=index_name)
    data_frame = clean_data_frame(data_frame)
    return data_frame
