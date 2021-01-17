from fp11recipes.freqtrackercpp import FreqTracker

pdict = {
    "nregions": [],
    "sregions": [fwdpy11.ExpS(beg=0, end=1, weight=1, mean=0.2)],
    "recregions": [fwdpy11.PoissonInterval(0, 1, 1e-2)],
    "gvalue": [fwdpy11.Multiplicative(2.0)],
    "rates": (0.0, 1e-2, None),
    "simlen": 100,
}
params = fwdpy11.ModelParams(**pdict)
pop = fwdpy11.DiploidPopulation(100, 1.0)
rng = fwdpy11.GSLrng(42)
recorder = FreqTracker(0)
fwdpy11.evolvets(
    rng,
    pop,
    params,
    10,
    recorder,
    track_mutation_counts=True,
    suppress_table_indexing=False,
)
