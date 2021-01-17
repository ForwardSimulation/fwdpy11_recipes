pdict = {
    # Add a region for neutral mutations:
    "nregions": [fwdpy11.Region(0, 1, 1)],
    "sregions": [fwdpy11.ExpS(beg=0, end=1, weight=1, mean=0.2)],
    "recregions": [fwdpy11.PoissonInterval(0, 1, 1e-2)],
    "gvalue": [fwdpy11.Multiplicative(2.0)],
    # Add a mutation rate for neutral mutations:
    "rates": (1e-2, 1e-2, None),
    "simlen": 100,
}
params = fwdpy11.ModelParams(**pdict)
pop = fwdpy11.DiploidPopulation(100, 1.0)
rng = fwdpy11.GSLrng(54321)
recorder = PyFreqTracker(0)
fwdpy11.evolvets(
    rng,
    pop,
    params,
    1,  # Simplify every generation
    recorder,
    suppress_table_indexing=False,
)
