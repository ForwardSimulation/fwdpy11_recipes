def traj2df(trajectories: typing.Dict, N: int) -> pd.DataFrame:
    dfs = []
    for key, value in trajectories.items():
        df = pd.DataFrame(
            {
                "generation": np.arange(len(value), dtype=np.uint32) + key[0],
                "frequency": np.array(value) / (2 * N),
                "origin_time": [key[0]] * len(value),
                "position": [key[1]] * len(value),
                "effect_size": [key[2]] * len(value),
            }
        )
        dfs.append(df)
    return pd.concat(dfs)
