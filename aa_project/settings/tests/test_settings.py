""" Test Settings

This file is not set up to test the app itself.

It's merely a trivial example that will invoke the PyTest runner within
the testing of the CI/CD process
"""

import os

from aa_project.settings.base import DATABASES


class TestDatabaseIsSecurelyConfigured:
    def test_secure_database_setup(self):
        assert DATABASES['default']['NAME'] == os.environ['DB_NAME']
        assert DATABASES['default']['USER'] == os.environ['DB_USER']
        assert DATABASES['default']['HOST'] == os.environ['DB_HOST']
        assert DATABASES['default']['PASSWORD'] == os.environ['DB_PASS']
        assert DATABASES['default']['PORT'] == os.environ['DB_PORT']
