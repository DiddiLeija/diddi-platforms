"""
This subpackage is the 'template factory',
and also serves the templates for level
creators.
"""

import os
import shutil


def install_template(template_type):
    """
    Install the desired template on the current working directory.
    """
    called_from = os.path.dirname(__file__)
    if template_type == "map":
        shutil.copy2(os.path.join(called_from, "map_template.pyxres"), "my_map.pyxres")
    else:
        raise ValueError(f"Unrecognized argument: '{template_type}'")
