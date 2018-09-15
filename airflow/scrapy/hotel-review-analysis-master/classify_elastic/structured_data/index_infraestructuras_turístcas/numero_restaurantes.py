# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_infraestructuras_turísticas/Infraestructuras turísticas.xlsx"
sheet = 2
name_index = "index_turidata_number_restaurants"
type_index = "structured"

name_items = {
    "type_rows" : "year",
    "type_cols" : "type establishment"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 10,
    "end_col": 2,
    "start_value_row": 3,
    "start_value_col": 1
}
type_value = int

attributes_to_fixed={
    "place" : "Puerto de la Cruz"
}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, attributes_to_fixed = attributes_to_fixed)
