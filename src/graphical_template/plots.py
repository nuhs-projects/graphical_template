import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from src.graphical_template import theme

def get_gradient_cmap(name="custom_brand", n_colors=10):
    colors = list(theme.BRAND_COLORS.values())
    cmap = mcolors.LinearSegmentedColormap.from_list(name, colors, N=n_colors)
    return cmap

def NUHS_bar_chart(labels, values, title=None):
    cmap = get_gradient_cmap(n_colors=len(values))
    colors = [cmap(i) for i in range(len(values))]

    # n = len(labels)
    # font_size = max(8, 16 - n // 2)

    fig, ax = plt.subplots(constrained_layout=True)
    ax.bar(labels, values, color=colors)

    if title is not None:
        ax.set_title(title)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)

    # Apply font and size to all tick labels
    for label in (ax.get_xticklabels()):
        label.set_fontproperties(theme.font_prop)
        # label.set_fontsize(font_size)

    plt.show()


def NUHS_stacked_bar_chart(labels, data, category_names, title = None):
    if len(category_names) == 1:
        raise ValueError("Stacked bar chart requires at least two categories.")

    data = np.array(data)
    n_categories = data.shape[0]
    n_bars = data.shape[1]

    # Get consistent colors
    if n_categories <= len(theme.BRAND_COLORS):
        colors = list(theme.BRAND_COLORS.values())[:n_categories]
    else:
        cmap = get_gradient_cmap(n_colors=n_categories)
        colors = [cmap(i) for i in range(n_categories)]

    fig, ax = plt.subplots(constrained_layout=True)
    bottom = np.zeros(n_bars)

    for i in range(n_categories):
        ax.bar(labels, data[i], bottom=bottom, color=colors[i], label=category_names[i])
        bottom += data[i]

    if title is not None:
        ax.set_title(title)

    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontname(theme.font_name)

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    # plt.tight_layout()
    plt.show()

def NUHS_grouped_bar_chart(labels, data, category_names, title=None):
    if len(category_names) == 1:
        raise ValueError("Grouped bar chart requires at least two categories.")

    data = np.array(data)  # shape: (n_categories, n_bars)
    n_categories, n_bars = data.shape

    x = np.arange(n_bars)  # label locations
    bar_width = 0.8 / n_categories  # dynamic spacing

    # Get consistent colors
    if n_categories == 2:
        colors = list(theme.BRAND_COLORS.values())[-2::-2]
    elif n_categories <= len(theme.BRAND_COLORS):
        colors = list(theme.BRAND_COLORS.values())[:n_categories]
    else:
        cmap = get_gradient_cmap(n_colors=n_categories)
        colors = [cmap(i) for i in range(n_categories)]

    fig, ax = plt.subplots(constrained_layout=True)

    for i in range(n_categories):
        ax.bar(x + i * bar_width, data[i], width=bar_width, label=category_names[i], color=colors[i])

    ax.set_xticks(x + bar_width * (n_categories - 1) / 2)
    ax.set_xticklabels(labels, fontname=theme.font_name)

    if title is not None:
        ax.set_title(title)

    for label in ax.get_yticklabels():
        label.set_fontname(theme.font_name)

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
    ax.set_ylim(0, data.max() * 1.1)

    plt.show()
