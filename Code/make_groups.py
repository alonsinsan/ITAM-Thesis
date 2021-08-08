def make_groups(X):
    # quantiles and make groups ()
    n = X.shape[1]
    division = X
    division['quantiles_group'] = ""
    for i in range(n):
        division.iloc[:,i] = pd.qcut(X.iloc[:,i], q = 4).astype(str)
        division['quantiles_group'] = division.quantiles_group + " & " + division.iloc[:,i]
    return division