import pytest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.stackplot import stackplot # Replace 'your_module' with the actual module name

@pytest.fixture
def setup_axes():
    fig, ax = plt.subplots()
    yield ax
    plt.close(fig)

def test_stackplot_zero_baseline(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    stackplot(ax, x, y1, y2, baseline='zero')
    assert len(ax.collections) == 2

def test_stackplot_sym_baseline(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    stackplot(ax, x, y1, y2, baseline='sym')
    assert len(ax.collections) == 2

def test_stackplot_wiggle_baseline(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    stackplot(ax, x, y1, y2, baseline='wiggle')
    assert len(ax.collections) == 2

def test_stackplot_weighted_wiggle_baseline(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    stackplot(ax, x, y1, y2, baseline='weighted_wiggle')
    assert len(ax.collections) == 2

def test_stackplot_colors(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    colors = ['#FF0000', '#00FF00']
    stackplot(ax, x, y1, y2, colors=colors)
    assert ax.collections[0].get_facecolor()[0][:3] == (1.0, 0.0, 0.0)
    assert ax.collections[1].get_facecolor()[0][:3] == (0.0, 1.0, 0.0)

def test_stackplot_hatch(setup_axes):
    ax = setup_axes
    x = np.arange(10)
    y1 = np.sin(x)
    y2 = np.cos(x)
    hatch = ['/', '\\']
    stackplot(ax, x, y1, y2, hatch=hatch)
    assert ax.collections[0].get_hatch() == '/'
    assert ax.collections[1].get_hatch() == '\\'

if __name__ == '__main__':
    pytest.main()
