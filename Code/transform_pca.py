def transform_pca(dmat, n, id_column):
    # train and transform PCA (number of components)
    dmat.index = dmat[id_column]
    dmat = dmat.drop(id_column, axis = 1)
    components = pd.DataFrame(data = pca.fit_transform(dmat), index = dmat.index)
    return components