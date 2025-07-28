#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.org"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import PropertyMock
from parameterized import parameterized
from fixtures import TEST_PAYLOAD
from parameterized import parameterized_class
import requests


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected result"""
        expected_payload = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
# inside the TestGithubOrgClient class
def test_public_repos_url(self):
    """Test that _public_repos_url returns correct repos_url from org"""
    expected_repos_url = "https://api.github.com/orgs/google/repos"
    mock_payload = {"repos_url": expected_repos_url}

    with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
        mock_org.return_value = mock_payload
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, expected_repos_url)
@patch("client.get_json")
def test_public_repos(self, mock_get_json):
    """Test that public_repos returns correct repo names"""
    expected_repos = ["repo1", "repo2"]
    mock_payload = [
        {"name": "repo1"},
        {"name": "repo2"},
    ]
    mock_get_json.return_value = mock_payload

    with patch.object(GithubOrgClient, "_public_repos_url", return_value="http://mocked_url") as mock_url:
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, expected_repos)
        mock_get_json.assert_called_once_with("http://mocked_url")
        mock_url.assert_called_once()
# Inside TestGithubOrgClient class
@parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False),
])
def test_has_license(self, repo, license_key, expected):
    """Test has_license returns correct boolean based on license key"""
    client = GithubOrgClient("test_org")
    result = client.has_license(repo, license_key)
    self.assertEqual(result, expected)
@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD["org_payload"],
        "repos_payload": TEST_PAYLOAD["repos_payload"],
        "expected_repos": TEST_PAYLOAD["expected_repos"],
        "apache2_repos": TEST_PAYLOAD["apache2_repos"]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Start patching requests.get with fixture-based side_effect"""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                mock_resp = unittest.mock.Mock()
                mock_resp.json.return_value = cls.org_payload
                return mock_resp
            elif url == cls.org_payload["repos_url"]:
                mock_resp = unittest.mock.Mock()
                mock_resp.json.return_value = cls.repos_payload
                return mock_resp
            return None

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get"""
        cls.get_patcher.stop()
