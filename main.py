"""
This 'main file' is the one that should be
distributed as the main game. It only wraps
a few operations with the 'diddiplatforms_pkg'
package, but nothing else is involved.
"""

from diddiplatforms_pkg.runner import AppRunner

AppRunner()
