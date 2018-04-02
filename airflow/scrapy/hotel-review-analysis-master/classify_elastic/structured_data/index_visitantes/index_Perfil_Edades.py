import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_visitantes/visitantes.xlsx"
sheet = 0
name_index = "index_perfil_turistico"
type_index = "structured"

name_items = {
    "type_rows" : "place_tourist_residence",
    "type_cols" : "year",
    "subtype_rows" : "gender",
    "subtype_cols" :"age"
}


table_start_and_end = {
    "start_row": 2,
    "start_col": 0,
    "end_row": 15,
    "end_col": 21,
    "start_value_row": 4,
    "start_value_col": 1
}
type_value = int

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value)
