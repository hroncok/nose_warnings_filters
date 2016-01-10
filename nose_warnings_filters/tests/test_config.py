import nose_warnings_filters as nwf
import warnings

import nose.tools as nt


import nose_warnings_filters

def test():
    nwf.WarningFilter()
    
def test_ignore():
    with warnings.catch_warnings(record=True) as w:
        warnings.warn('This should be ignored', nose_warnings_filters.MyWarningIgnore)
        nt.assert_equals(w, [])

def test_error():
    with nt.assert_raises(nose_warnings_filters.MyWarningError):
        warnings.warn('This should error', nose_warnings_filters.MyWarningError)
