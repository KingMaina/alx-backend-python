#!/usr/bin/env python3
"""Tests the GitHubOrgClient class"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized, param, parameterized_class
from unittest.mock import patch, PropertyMock
from typing import List, Mapping
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GitHubOrgClient"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Tests GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))

    @parameterized.expand([
        ('some_org', {'repos_url': 'https://api.github.com/orgs/some_org'}),
    ])
    def test_public_repos_url(self, org_name, expected):
        """Tests the public repos URL is returned"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock(
            return_value=expected
        )):
            response = GithubOrgClient(org_name)._public_repos_url
            self.assertEqual(response, expected.get('repos_url'))
            self.assertRegex(response, '{}'.format(org_name))

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json, license=None):
        """Tests that public repos are fetched"""
        url = 'https://api.github.com/orgs/some_org'
        payload_repos = [
            {'name': 'MyFirstRepo'},
            {'name': 'MyOtherRepo'}
        ]
        mock_get_json.return_value = payload_repos
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo_url:
            repos: List[str] = GithubOrgClient(
                org_name='some_org').public_repos(license)
            mock_repo_url.return_value = url
            payload_values = [name['name'] for name in payload_repos]
            self.assertListEqual(repos, payload_values)
            mock_get_json.assert_called_once()
            mock_repo_url.assert_called_once()

    @parameterized.expand([
        param(repo={"license": {"key": "my_license"}},
              license_key="my_license",
              expected=True),
        param(repo={"license": {"key": "other_license"}},
              license_key="my_license",
              expected=False)
    ])
    def test_has_license(self, repo: Mapping, license_key: str,
                         expected: bool) -> None:
        """Test the presence of a license"""
        isLicensePresent = GithubOrgClient(
            'some_org').has_license(repo, license_key)
        self.assertEqual(isLicensePresent, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up tests"""
        config = {'return_value.json.side_effect':
                  [cls.org_payload, cls.repos_payload,
                  cls.org_payload, cls.repos_payload]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration tests for fetching public repos"""
        google_repo = GithubOrgClient(org_name='google')
        self.assertEqual(google_repo.org, self.org_payload)
        self.assertEqual(google_repo.repos_payload, self.repos_payload)
        self.assertEqual(google_repo.public_repos(), self.expected_repos)
        self.assertEqual(google_repo.public_repos(license='apache-2.0'),
                         self.apache2_repos)

    def test_public_repos_with_license(self):
        """Tests public repos with apache-2.0 license"""
        repo = GithubOrgClient(org_name='google')
        apache2_repos = repo.public_repos(license='apache-2.0')
        self.assertEqual(apache2_repos, self.apache2_repos)
