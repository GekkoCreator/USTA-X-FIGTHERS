# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:46:34 2023

@author: jfern
"""

import pandas as pd
sheet_id = '1b17dzk-MyURmut3UsNkk0ynrsVuq5CKIrK-R8p4JNjc'
sheet_name = 'data'
url = 'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
base_data = pd.read_csv(url)
 