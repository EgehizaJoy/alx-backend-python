#!/usr/bin/env python3
"""Unit tests for GithubOrgClient.org"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import PropertyMock
from parameterized import parameterized

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
