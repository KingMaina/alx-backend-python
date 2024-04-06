#!/usr/bin/env python3

"""Unittests for the utils class"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function"""

    @parameterized.expand([
        param(1, nested_map={"a": 1}, path=("a",)),
        param({"b": 2}, nested_map={"a": {"b": 2}}, path=("a",)),
        param(2, nested_map={"a": {"b": 2}}, path=("a", "b")),
    ])
    def test_access_nested_map(self, expected: Any,
                               nested_map: Mapping,
                               path: Sequence) -> None:
        """Test if function accesses a mapped object"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        param(nested_map={}, path=("a",), expected="a"),
        param(nested_map={"a": 1}, path=("a", "b"), expected="b"),
    ])
    def test_access_nested_map_exception(self, expected: Any,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """Tests if exception is raised for invalid keys"""
        with self.assertRaises(KeyError, msg=expected) as context_manager:
            access_nested_map(nested_map=nested_map, path=path)
        self.assertEqual(expected, context_manager.msg)


class TestGetJson(unittest.TestCase):
    """Unittests for the `get_json` function"""

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    def test_get_json(self, test_payload, test_url):
        """Tests that JSON data is received from API call"""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock_get_json = patcher.start()
        self.assertEqual(get_json(url=test_url), test_payload)
        mock_get_json.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Test memoizing a value"""

    def test_memoize(self):
        """Tests memoizing functionality"""
        class TestClass:
            """Test class"""

            def a_method(self):
                """Returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Returns mememoized value of `a_method`"""
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
