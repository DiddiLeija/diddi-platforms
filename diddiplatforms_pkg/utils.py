"""
Misc utils that are used by this package.
"""

import warnings


def warn(msg, warning_type=UserWarning):
    # Used a separate space to hide information
    # shown by the stack level.
    warnings.warn(msg)
