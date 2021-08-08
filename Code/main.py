def create_experimental_group(n_components, size, path, id_column, group):
    """Script for creating an experimental group with a design matrix."""
    if (size >= 4**n_components):
        dmat = pd.read_csv(path)
        dmat = dmat[dmat.group == group].drop('group', axis=1)
        dmat = validate_matrix(dmat, id_column)
        components = transform_pca(dmat, n_components, id_column)
        division = make_groups(components)
        groups = iterate_division(division, size, n_components)
        groups.to_csv('/pfs/out/prueba_piloto.csv')
    else:
        click.echo(f'Error: minimum size should be {4**n_components}')