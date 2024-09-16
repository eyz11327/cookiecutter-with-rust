import logging
import ctypes
logger = logging.getLogger("init")

def run(rust_lib, secret_config, cwd):
    logger.info("Hello {{ cookiecutter.project_slug | replace('-', '_')}}!")

    rust_lib.compute_square.argtypes = [ctypes.c_double]
    rust_lib.compute_square.restype = ctypes.c_double

    number = 3.0
    # Using rust
    result = rust_lib.compute_square(number)
    logger.info(f"Rust: The square of {number} is {result}")
    # Using python
    result = number * number
    logger.info(f"Python: The square of {number} is {result}")

    logger.info("Goodbye.")