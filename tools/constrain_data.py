import click
import json

import pandas as pd
import geopandas as gpd

from utils import reindex_data_frame, select_and_rename_columns


"""
selects a subset of data and renames it as per the config file
"""


@click.command()
@click.option("--index", default="index")
@click.option("--output", default="out.geojson", type=click.Path(dir_okay=False))
@click.argument("columns", type=click.File("r"))
@click.argument("data", type=click.File("r"))
def constrain_data(index, output, columns, data):
    import pdb; pdb.set_trace()
    columns = json.load(columns)
    geo_data_frame = gpd.read_file(data)
    geo_data_frame = reindex_data_frame(geo_data_frame)
    constrained_geo_data_frame = select_and_rename_columns(geo_data_frame, columns, ignore_missing=True)
    constrained_geo_data_frame.to_file(output, driver="GeoJSON")


if __name__ == "__main__":
    constrain_data()
