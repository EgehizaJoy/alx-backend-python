# 0x03. Unittests and Integration Tests

This project focuses on writing **unit tests** and **integration tests** in Python using the `unittest` framework. You'll also explore techniques like **mocking**, **parameterized testing**, and **memoization**.

## 📚 Learning Objectives

By the end of this project, you should be able to:

- Distinguish between **unit tests** and **integration tests**
- Apply **mocking** to isolate external dependencies
- Use `parameterized` to run multiple test cases
- Understand and use **fixtures**
- Apply memoization and test for side-effect-free functions

## 🧪 Files and Descriptions

| File | Description |
|------|-------------|
| `utils.py` | Utility functions like `access_nested_map`, `get_json`, and a `memoize` decorator |
| `client.py` | A GitHub organization client that fetches org and repo info from GitHub’s API |
| `fixtures.py` | Contains test payloads used in integration tests |
| `test_utils.py` | Unit tests for `utils.py` |
| `test_client.py` | Unit and integration tests for `client.py` |

## ✅ Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Follow `pycodestyle` (v2.5)
- Use `unittest` and `unittest.mock`
- All files should be executable and have documentation
- Functions must be type-annotated

## 🛠️ Run Tests

To run the unit and integration tests:

```bash
python3 -m unittest discover 0x03-Unittests_and_integration_tests
