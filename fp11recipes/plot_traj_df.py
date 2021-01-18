import matplotlib.pyplot as plt
import pandas as pd


def plot_traj_df(
    df: pd.DataFrame, *, minlen: int, selected_alpha=1.0, neutral_alpha=1.0
) -> None:
    if minlen < 0:
        raise ValueError(f"minlen must be non-negative, got {minlen}")
    plt.figure()
    for n, g in df.groupby(["origin_time", "position", "effect_size"]):
        if len(g.index) >= minlen:
            if g.effect_size[0] == 0.0:
                plt.plot(g.generation, g.frequency, linestyle="--", alpha=neutral_alpha)
            else:
                plt.plot(g.generation, g.frequency, alpha=selected_alpha)
    plt.xlabel("Time (generation)")
    plt.ylabel("Frequency")
    plt.show()
