"""flask-ligand test fixtures and helper functions."""

# ======================================================================================================================
# Imports
# ======================================================================================================================
from __future__ import annotations
import re
import time
import uuid
import flask
import pytest
from datetime import datetime
from typing import TYPE_CHECKING
from dateutil.parser import parse


# ======================================================================================================================
# Type Checking
# ======================================================================================================================
if TYPE_CHECKING:
    from typing import Any


# ======================================================================================================================
# Globals
# ======================================================================================================================
__version__ = "0.1.4"
DUMMY_ID = str(uuid.UUID("00000000-0000-0000-0000-000000000000"))
DUMMY_ETAG = "0000000000000000000000000000000000000000"
USER_ID = DUMMY_ID
USER_DEFAULT_ROLES = ["admin", "user"]
OPEN_API_CLIENT_NAME = "ligand-client"
ISO_8601_REGEX = (
    r"^(?:[1-9]\d{3}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|"
    r"(?:0[13578]|1[02])-31)|(?:[1-9]\d(?:0[48]|[2468][048]|[13579][26])|"
    r"(?:[2468][048]|[13579][26])00)-02-29)T(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\dZ$"
)


# ======================================================================================================================
# Classes: Private
# ======================================================================================================================
class FlaskLigandTestHelpers(object):
    """A collection of helper functions for testing flask-ligand microservices."""

    @staticmethod
    def is_sub_dict(small: dict[Any, Any], big: dict[Any, Any]) -> bool:
        """Determine if one dictionary is a subset of another dictionary.

        Args:
            small: A dictionary that is proposed to be a subset of another dictionary.
            big: A dictionary that is a superset of another dictionary.

        Returns:
            A bool indicating if the small dictionary is in fact a sub-dictionary of big
        """

        return dict(big, **small) == big

    @staticmethod
    def wait(seconds: int | float) -> None:
        """Wait for a set amount of time in seconds.

        Args:
            seconds: The amount of time to wait.
        """

        time.sleep(seconds)

    @staticmethod
    def parse_iso_str(iso_8601_str: str) -> datetime:
        """Parse an ISO 8601 string into a datetime object.

        Args:
            iso_8601_str: An ISO 8601 string to parse.
        """

        return parse(iso_8601_str)

    @staticmethod
    def loads(s: str) -> Any:
        """Deserialize a JSON string into a dictionary.

        Args:
            s: JSON string to deserialize.
        """

        return flask.json.loads(s)


# ======================================================================================================================
# Fixtures: Public
# ======================================================================================================================
@pytest.fixture(scope="session")
def helpers() -> FlaskLigandTestHelpers:
    """A collection of helper functions for testing flask-ligand microservices."""

    return FlaskLigandTestHelpers()


@pytest.fixture(scope="session")
def dummy_id() -> str:
    """A dummy UUID to use for negative test cases."""

    return DUMMY_ID


@pytest.fixture(scope="session")
def dummy_etag() -> str:
    """A dummy ETag to use for negative test cases."""

    return DUMMY_ETAG


@pytest.fixture(scope="session")
def iso_8601_datetime_rgx() -> re.Pattern[str]:
    """A regular expression for the expected datetime format for all schemas."""

    return re.compile(ISO_8601_REGEX)


@pytest.fixture(scope="function")
def default_roles() -> list[str]:
    """A list of default roles to use for gaining access to endpoints. (By default this grants admin access)."""

    return USER_DEFAULT_ROLES


@pytest.fixture(scope="function")
def user_info(default_roles: list[str]) -> dict[str, Any]:
    """A dictionary containing the user information used for authentication in the JWT."""

    return {
        "id": USER_ID,
        "roles": default_roles,
    }


@pytest.fixture(scope="session")
def open_api_client_name() -> str:
    """The client name to use for the OpenAPI generator endpoints."""

    return OPEN_API_CLIENT_NAME
