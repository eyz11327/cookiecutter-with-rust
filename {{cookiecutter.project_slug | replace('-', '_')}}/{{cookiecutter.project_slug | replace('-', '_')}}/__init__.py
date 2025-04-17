import logging
from typing import Any, TypedDict
from {{ cookiecutter.project_slug | replace('-', '_')}}_rust._rust_functions import add_numbers
logger = logging.getLogger("init")

class SecretConfig(TypedDict):
    username: str

def run(secret_config: SecretConfig, cwd: str) -> None:
    logger.info("Hello {{ cookiecutter.project_slug | replace('-', '_')}}!")

    example_number: float = 5.5123
    example_number2: float = 7.882

    # Using rust
    result: float = add_numbers(example_number, example_number2)
    logger.info(f"Rust: The result of {example_number} + {example_number2} is {result}")
    # Using python
    result = example_number + example_number2
    logger.info(f"Python: The result of {example_number} + {example_number2} is {result}")

    logger.info("Goodbye.")