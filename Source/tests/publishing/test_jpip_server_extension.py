import os.path
import shutil

import arcpyext
import pytest

from arcpyext.publishing._jpip_server_extension import JpipServerExtension
from arcpyext.publishing._sddraft_editor import SDDraftEditor
from .. helpers import *

SDDRAFT_FILE_PATH = os.path.abspath("{0}/../samples/imageservice.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_SAVE_TEST_FILE_PATH = os.path.abspath("{0}/../samples/imageservice.savetest.sddraft".format(os.path.dirname(__file__)))
SDDRAFT_FILE_PATH_COPY = os.path.abspath("{0}/../samples/imageservice.copy.sddraft".format(os.path.dirname(__file__)))

@pytest.fixture
def server_ext():
    shutil.copyfile(SDDRAFT_FILE_PATH, SDDRAFT_FILE_PATH_COPY)
    return JpipServerExtension(SDDraftEditor(SDDRAFT_FILE_PATH_COPY))

def test_capabilities(server_ext):
    assert isinstance(type(server_ext).capabilities, property) == True
    assert server_ext.capabilities == None
    with pytest.raises(NotImplementedError):
        server_ext.capabilities = "Blah"