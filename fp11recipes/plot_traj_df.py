import typing

import matplotlib.pyplot as plt
import pandas as pd


def plot_traj_df(
    df: pd.DataFrame, *, minlen: int, selected_alpha=1.0, neutral_alpha=1.0
) -> typing.Tuple:
    if minlen < 0:
        raise ValueError(f"minlen must be non-negative, got {minlen}")
    f, ax = plt.subplots()
    for n, g in df.groupby(["origin_time", "position", "effect_size"]):
        if len(g.index) >= minlen:
            if g.effect_size[0] == 0.0:
                ax.plot(g.generation, g.frequency, linestyle="--", alpha=neutral_alpha)
            else:
                ax.plot(g.generation, g.frequency, alpha=selected_alpha)
    ax.set_xlabel("Time (generation)")
    ax.set_ylabel("Frequency")

    return f, ax
