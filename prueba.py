import pandas as pd
import numpy as np

# Ejemplo: Producción diaria (en unidades)
produccion = pd.Series([100, 120, 110, 130, 115, 125, 120],
                       index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
print(produccion)