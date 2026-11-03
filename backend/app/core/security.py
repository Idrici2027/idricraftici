
"""Password security utilities for IDRICI CRAFT."""

import hashlib
import hmac
import secrets

ALGORITHM = "sha256"
ITERATIONS = 600_000
SALT_SIZE = 16


def hash_password(password: str) -> str:
    """Hash a password using PBKDF2-HMAC-SHA256."""

    if not password:
        raise ValueError("Password cannot be empty")

    salt = secrets.token_bytes(SALT_SIZE)

    password_hash = hashlib.pbkdf2_hmac(
        ALGORITHM,
        password.encode("utf-8"),
        salt,
        ITERATIONS,
    )

    return (
        f"pbkdf2_{ALGORITHM}${ITERATIONS}$"
        f"{salt.hex()}${password_hash.hex()}"
    )


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against its stored hash."""

    try:
        algorithm, iterations, salt_hex, hash_hex = stored_hash.split("$")

        if algorithm != f"pbkdf2_{ALGORITHM}":
            return False

        rounds = int(iterations)

        if rounds < 1 or rounds > 2_000_000:
            return False

        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)

        if len(salt) != SALT_SIZE:
            return False

        actual_hash = hashlib.pbkdf2_hmac(
            ALGORITHM,
            password.encode("utf-8"),
            salt,
            rounds,
        )

        return hmac.compare_digest(actual_hash, expected_hash)

    except (ValueError, TypeError, AttributeError):
        return False
