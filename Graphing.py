import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_data(x_name, y_name, data_df, ax=None, **kwargs):
    print("plotting")

    if ax is None:
        ax = plt.gca()

    print(x_name)
    print(y_name)

    if not x_name or not y_name:
        return

    try:
        print(x_name)
        x_data = data_df[x_name]  # Access column using x_name directly
        y_data = data_df[y_name]

        x_data = pd.to_numeric(x_data, errors='coerce')
        y_data = pd.to_numeric(y_data, errors='coerce')

        x_data[np.isnan(x_data)] = np.nan
        y_data[np.isnan(y_data)] = np.nan

        ax.plot(x_data, y_data, marker='o', linestyle='-')

        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.set_title(f'Plot of {x_name} vs {y_name}')
        ax.grid(True)

        plt.subplots_adjust(left=0.25, bottom=0.25)

        plt.show()

    except Exception as e:
        print(f"Error updating plot: {e}")

