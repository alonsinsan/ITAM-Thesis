def iterate_division(division, size, n_components):
    m = division.groupby('quantiles_group')[0].count()
    m = m[m>size/n_components].index
    experimental = []
    for group in m:
        empresarias = division[division.quantiles_group == group].index
        aux = sample(list(empresarias), round(size/len(m)))
        experimental.append(aux)
    division['indicador'] = 'control'
    experimental = [item for sublist in experimental for item in sublist]
    division.loc[division.index.isin(experimental), 'indicador'] = 'experimental'
    return division