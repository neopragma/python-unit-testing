---
applyTo: '**/*.py**'
---
# Copilot Instructions

When generating code, always prioritize writing unit tests first. This ensures that the production code is well-tested and meets the requirements. Focus on edge cases and error handling in your tests. Use descriptive names for test functions to make them easily understandable. If the code is complex, consider breaking it down into smaller, testable functions. Use assertions to verify that the outcomes are as expected. If you have any questions or need clarification, don't hesitate to ask before proceeding with the implementation.

Production source goes in subdirectory `src/`. The tests go in the subdirectory `tests/`.
If you need to import modules, use relative imports like this:
from ..src.module_name import function_name
If you need to import modules from the same directory, use absolute imports like this:
from src.module_name import function_name
If you need to import modules from the parent directory, use relative imports like this:
from ..module_name import function_name
If you need to import modules from the grandparent directory, use relative imports like this:
from ...module_name import function_name
If you need to import modules from the root directory, use absolute imports like this:
from src.module_name import function_name
