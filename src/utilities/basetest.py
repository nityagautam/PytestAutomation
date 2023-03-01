import pytest
from src.utilities.Logger import Logger


@pytest.mark.usefixtures("get_web_driver", "setup", "get_logger", "get_config")
class BaseTest:
    # ------------------------------------------------------------------
    # initialisations from the fixture methods
    # So that for each child Test class we will have
    # all the properties after inheriting this BaseTest class
    # ------------------------------------------------------------------
    driver = None
    config = None
    log = None

    # ------------------------------------------------------------------
    # Do anything extra for each test class
    # ------------------------------------------------------------------
    pass
