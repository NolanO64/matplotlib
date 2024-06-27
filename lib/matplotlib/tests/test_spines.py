import numpy as np
import pytest

import matplotlib.pyplot as plt
from matplotlib.spines import Spines
from matplotlib.testing.decorators import check_figures_equal, image_comparison


def test_spine_class():
    """Test Spines and SpinesProxy in isolation."""
    class SpineMock:
        def __init__(self):
            self.val = None

        def set(self, **kwargs):
            vars(self).update(kwargs)

        def set_val(self, val):
            self.val = val

    spines_dict = {
        'left': SpineMock(),
        'right': SpineMock(),
        'top': SpineMock(),
        'bottom': SpineMock(),
    }
    spines = Spines(**spines_dict)

    assert spines['left'] is spines_dict['left']
    assert spines.left is spines_dict['left']

    spines[['left', 'right']].set_val('x')
    assert spines.left.val == 'x'
    assert spines.right.val == 'x'
    assert spines.top.val is None
    assert spines.bottom.val is None

    spines[:].set_val('y')
    assert all(spine.val == 'y' for spine in spines.values())

    spines[:].set(foo='bar')
    assert all(spine.foo == 'bar' for spine in spines.values())

    with pytest.raises(AttributeError, match='foo'):
        spines.foo
    with pytest.raises(KeyError, match='foo'):
        spines['foo']
    with pytest.raises(KeyError, match='foo, bar'):
        spines[['left', 'foo', 'right', 'bar']]
    with pytest.raises(ValueError, match='single list'):
        spines['left', 'right']
    with pytest.raises(ValueError, match='Spines does not support slicing'):
        spines['left':'right']
    with pytest.raises(ValueError, match='Spines does not support slicing'):
        spines['top':]

from matplotlib.spines import branch_coverage, print_coverage

def setup_function(function):
    """Setup testing environment before each test function."""
    global branch_coverage
    branch_coverage = {key: False for key in branch_coverage}

def test_set_bounds_circle_raises_error():
    """Test if set_bounds on a circular spine raises the correct error."""
    spine = Spine(spine_type='circle')
    with pytest.raises(ValueError) as exc_info:
        spine.set_bounds(10, 20)
    assert "incompatible with circular spines" in str(exc_info.value)
    assert branch_coverage["set_bounds_1"], "Branch set_bounds_1 was not hit."

def test_set_bounds_iterable_low_high_none():
    """Test if set_bounds correctly unpacks iterable low when high is None."""
    spine = Spine()
    spine.set_bounds((5, 15))
    assert spine.get_bounds() == (5, 15), "Bounds were not correctly unpacked from iterable."
    assert branch_coverage["set_bounds_2"], "Branch set_bounds_2 was not hit."

def test_set_bounds_low_none_uses_old_low():
    """Test if set_bounds uses old low when low is None."""
    spine = Spine(bounds=(10, 20))
    spine.set_bounds(None, 30)
    assert spine.get_bounds() == (10, 30), "Old low was not used when low was None."
    assert branch_coverage["set_bounds_3"], "Branch set_bounds_3 was not hit."

def test_set_bounds_high_none_uses_old_high():
    """Test if set_bounds uses old high when high is None."""
    spine = Spine(bounds=(10, 20))
    spine.set_bounds(15, None)
    assert spine.get_bounds() == (15, 20), "Old high was not used when high was None."
    assert branch_coverage["set_bounds_4"], "Branch set_bounds_4 was not hit."

def test_coverage_after_tests():
    """Check coverage report after all tests have been run."""
    print_coverage()
    for value in branch_coverage.values():
        assert value, "Not all branches were covered."


@image_comparison(['spines_axes_positions'])
def test_spines_axes_positions():
    # SF bug 2852168
    fig = plt.figure()
    x = np.linspace(0, 2*np.pi, 100)
    y = 2*np.sin(x)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('centered spines')
    ax.plot(x, y)
    ax.spines.right.set_position(('axes', 0.1))
    ax.yaxis.set_ticks_position('right')
    ax.spines.top.set_position(('axes', 0.25))
    ax.xaxis.set_ticks_position('top')
    ax.spines.left.set_color('none')
    ax.spines.bottom.set_color('none')


@image_comparison(['spines_data_positions'])
def test_spines_data_positions():
    fig, ax = plt.subplots()
    ax.spines.left.set_position(('data', -1.5))
    ax.spines.top.set_position(('data', 0.5))
    ax.spines.right.set_position(('data', -0.5))
    ax.spines.bottom.set_position('zero')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])


@check_figures_equal(extensions=["png"])
def test_spine_nonlinear_data_positions(fig_test, fig_ref):
    plt.style.use("default")

    ax = fig_test.add_subplot()
    ax.set(xscale="log", xlim=(.1, 1))
    # Use position="data" to visually swap the left and right spines, using
    # linewidth to distinguish them.  The calls to tick_params removes labels
    # (for image comparison purposes) and harmonizes tick positions with the
    # reference).
    ax.spines.left.set_position(("data", 1))
    ax.spines.left.set_linewidth(2)
    ax.spines.right.set_position(("data", .1))
    ax.tick_params(axis="y", labelleft=False, direction="in")

    ax = fig_ref.add_subplot()
    ax.set(xscale="log", xlim=(.1, 1))
    ax.spines.right.set_linewidth(2)
    ax.tick_params(axis="y", labelleft=False, left=False, right=True)


@image_comparison(['spines_capstyle'])
def test_spines_capstyle():
    # issue 2542
    plt.rc('axes', linewidth=20)
    fig, ax = plt.subplots()
    ax.set_xticks([])
    ax.set_yticks([])


def test_label_without_ticks():
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.3, bottom=0.3)
    ax.plot(np.arange(10))
    ax.yaxis.set_ticks_position('left')
    ax.spines.left.set_position(('outward', 30))
    ax.spines.right.set_visible(False)
    ax.set_ylabel('y label')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines.bottom.set_position(('outward', 30))
    ax.spines.top.set_visible(False)
    ax.set_xlabel('x label')
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    plt.draw()

    spine = ax.spines.left
    spinebbox = spine.get_transform().transform_path(
        spine.get_path()).get_extents()
    assert ax.yaxis.label.get_position()[0] < spinebbox.xmin, \
        "Y-Axis label not left of the spine"

    spine = ax.spines.bottom
    spinebbox = spine.get_transform().transform_path(
        spine.get_path()).get_extents()
    assert ax.xaxis.label.get_position()[1] < spinebbox.ymin, \
        "X-Axis label not below the spine"


@image_comparison(['black_axes'])
def test_spines_black_axes():
    # GitHub #18804
    plt.rcParams["savefig.pad_inches"] = 0
    plt.rcParams["savefig.bbox"] = 'tight'
    fig = plt.figure(0, figsize=(4, 4))
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor((0, 0, 0))
