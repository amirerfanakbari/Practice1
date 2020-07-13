sale_jari = int(input('geymat sale jari:'))
sale_gabl = int(input('geymat sale gabl:'))
tavarom = float((sale_jari - sale_gabl) / sale_gabl)
sale_baed = (sale_gabl + sale_jari) * tavarom
print('sale_baed', sale_baed)
