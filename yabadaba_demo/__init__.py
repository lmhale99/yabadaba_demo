# coding: utf-8
# Standard Python libraries
from importlib import resources

# Read version from VERSION file
if hasattr(resources, 'files'):
    __version__ = resources.files('yabadaba_demo').joinpath('VERSION').read_text(encoding='UTF-8')
else:
    __version__ = resources.read_text('yabadaba_demo', 'VERSION', encoding='UTF-8').strip()


from . import record