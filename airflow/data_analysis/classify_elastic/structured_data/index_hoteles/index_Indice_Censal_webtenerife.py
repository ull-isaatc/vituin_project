# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/tcpuerto201809.xlsx"
sheet = 39
name_index = "index_indice_censal_webtenerife"
type_index = "structured"


name_items = {
    "type_rows" : "month",
    "type_cols" : "place",
    "subtype_cols" :"accomodation"
}


table_start_and_end = {
    "start_row": 4,
    "start_col": 1,
    "end_row": 18,
    "end_col": 46,
    "start_value_row": 6,
    "start_value_col": 2
}
type_value = float



add_column_value_to_previous_item = [{
    "type_item":"subtype_cols",
    "name_item":"interanual variation",
    "name":"variación interanual"
}]

involved_elements =[{"name":"Santa Cruz","number":4,"type":"less"}]
irregular_table = [{"type":"sum", "name_item":"subtype_cols", "number":4, "involved_elements": involved_elements}]

value_percentage = True

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, value_percentage = value_percentage, \
                        irregular_table = irregular_table,  add_column_value_to_previous_item = add_column_value_to_previous_item)
