def calculate_sfi(epl, npl, ets, nts, eit, nit):
    """
    Calculate the Sciatic Functional Index (SFI).

    Parameters:
    epl (float): Experimental paw length (heel to third toe) for the right paw.
    npl (float): Normal paw length for the left paw.
    ets (float): Experimental toe spread (distance between first and fifth toes) for the right paw.
    nts (float): Normal toe spread for the left paw.
    eit (float): Experimental inter-median toe spread (distance between second and fourth toes) for the right paw.
    nit (float): Normal inter-median toe spread for the left paw.

    Returns:
    float: The calculated SFI value.
    """
    sfi = (-38.3 * ((epl - npl) / npl) +
           109.5 * ((ets - nts) / nts) +
            13.3 * ((eit - nit) / nit) -
           8.839)
    
    return sfi