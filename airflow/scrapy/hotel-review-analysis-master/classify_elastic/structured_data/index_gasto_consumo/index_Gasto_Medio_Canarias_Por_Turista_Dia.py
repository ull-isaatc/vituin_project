# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from structured_data import index_excels_Istac

excel = "excels_gasto_consumo/gasto.xls"
sheet = 0
name_index = "index_gasto_por_residencia"
type_index = "structured"

name_items = {
    "type_rows" : "type",
    "subtype_rows" : "place",
    "type_cols" : "attribute_to_split_0",
    "subtype_cols" :"place_tourist_residence"
}


table_start_and_end = {
    "start_row": 216,
    "start_col": 0,
    "end_row": 240,
    "end_col": 173,
    "start_value_row": 218,
    "start_value_col": 1
}
type_value = float

attribute_to_split = [{
    "attributes":["year","trimester"],  #Attributes to split
    "attr0":[0],                        #Words by attribute 0
    "attr1":[1,2]                       #Words by attribute 1
}]

field_region = ["place_tourist_residence"]

fixed_attributes={
    "shop place": "canarias",
    "period":"dia"
}

fields_to_change = {'TOTAL PAISES' : 'Total'}

index_excels_Istac.main(excel, sheet, name_index, type_index, name_items, table_start_and_end, type_value, fixed_attributes = fixed_attributes, attribute_to_split = attribute_to_split, field_region = field_region, fields_to_change = fields_to_change)
