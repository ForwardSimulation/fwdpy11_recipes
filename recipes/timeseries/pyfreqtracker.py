@attr.s(auto_attribs=True)
class PyFreqTracker(object):
    burnin_time: int
    trajectories: typing.Dict = attr.ib(default=attr.Factory(dict))

    def __call__(
        self, pop: fwdpy11.DiploidPopulation, sampler: fwdpy11.SampleRecorder
    ) -> None:
        if pop.generation > self.burnin_time:
            for c, m in zip(pop.mcounts, pop.mutations):
                if c > 0 and c <= 2 * pop.N:
                    k = (m.g, m.pos, m.s)
                    if k in self.trajectories:
                        # Make sure that we only record a fixation once.
                        if self.trajectories[k][-1] < 2 * pop.N:
                            self.trajectories[k].append(c)
                    else:
                        self.trajectories[k] = [c]
