import pytest
import matplotlib
from unittest.mock import patch, MagicMock
from matplotlib import pyplot as plt, rcsetup, cbook
from matplotlib.pyplot import switch_backend, coverage_info, print_coverage_info  # Adjust the import based on the relative path

@pytest.fixture(autouse=True)
def reset_coverage_info():
    global coverage_info
    coverage_info = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False
    }
    yield
    print_coverage_info()

def test_auto_backend_sentinel():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'):
        switch_backend('auto')
    assert coverage_info[1] is True

def test_fallback_to_agg():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'), \
         patch('matplotlib.cbook._get_running_interactive_framework', return_value=None), \
         patch('matplotlib.pyplot.switch_backend') as mock_switch_backend:
        mock_switch_backend.side_effect = ImportError
        switch_backend('auto')
    assert coverage_info[2] is True

def test_interactive_framework_check():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'), \
         patch('matplotlib.cbook._get_running_interactive_framework', return_value='TkAgg'), \
         patch('matplotlib.backends.backend_registry.backends', return_value={'tkagg': 'TkAgg'}), \
         patch('matplotlib.backends.backend_registry.FigureCanvasTkAgg.required_interactive_framework', 'TkAgg'):
        switch_backend('tkagg')
    assert coverage_info[3] is True

def test_invalid_interactive_framework():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'), \
         patch('matplotlib.cbook._get_running_interactive_framework', return_value='Qt5Agg'), \
         patch('matplotlib.backends.backend_registry.backends', return_value={'tkagg': 'TkAgg'}), \
         patch('matplotlib.backends.backend_registry.FigureCanvasTkAgg.required_interactive_framework', 'TkAgg'):
        with pytest.raises(ImportError):
            switch_backend('tkagg')
    assert coverage_info[4] is True

def test_new_figure_manager_none():
    with patch('matplotlib.backends.backend_agg.FigureCanvasAgg.new_figure_manager', None), \
         patch('matplotlib.backends.backend_agg.FigureCanvasAgg.new_manager', return_value=None):
        switch_backend('agg')
    assert coverage_info[5] is True

def test_show_manager_class():
    with patch('matplotlib.backends.backend_agg.FigureCanvasAgg.new_figure_manager', None), \
         patch('matplotlib.backends.backend_agg.FigureCanvasAgg.new_manager', return_value=None), \
         patch('matplotlib.backends.backend_agg.FigureManagerBase.pyplot_show', new_callable=property):
        switch_backend('agg')
    assert coverage_info[6] is True

def test_switch_backend_normal_case():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'):
        switch_backend('agg')
    assert coverage_info[1] is False
    assert coverage_info[2] is False
    assert coverage_info[3] is False
    assert coverage_info[4] is False
    assert coverage_info[5] is False
    assert coverage_info[6] is False

def test_switch_backend_ipympl():
    with patch('matplotlib.rcsetup._auto_backend_sentinel', 'auto'), \
         patch('matplotlib.backends.backend', 'ipympl'), \
         patch('importlib.metadata.version', return_value='0.9.3'):
        switch_backend('ipympl')
    assert coverage_info[1] is False

if __name__ == '__main__':
    pytest.main()
