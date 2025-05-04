from hmac import digest_size

import pandas as pd
from numpy.ma.extras import column_stack

archive = pd.read_excel(r"assets/data-main.xlsx")
print(archive.dtypes)
print(archive.isnull().sum())
# Filtrar filas con client_email nulo y mostrar los product_id correspondientes
products_with_null_emails = archive[archive['client_email'].isnull()]['product_id']
print(products_with_null_emails)
