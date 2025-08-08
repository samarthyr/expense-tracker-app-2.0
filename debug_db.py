#!/usr/bin/env python
"""
Debug script to test database connection
"""
import os
import sys
from decouple import config

# Print environment variables (without sensitive data)
print("=== Environment Variables ===")
print(f"DB_NAME: {config('DB_NAME', default='NOT_SET')}")
print(f"DB_USER: {config('DB_USER', default='NOT_SET')}")
print(f"DB_HOST: {config('DB_HOST', default='NOT_SET')}")
print(f"DB_PORT: {config('DB_PORT', default='NOT_SET')}")
print(f"DB_PASSWORD: {'SET' if config('DB_PASSWORD', default=None) else 'NOT_SET'}")

# Test different connection configurations
import psycopg2
from psycopg2 import OperationalError

def test_connection(host, database, user, password, port=5432):
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port,
            sslmode='require'
        )
        print(f"✅ SUCCESS: Connected to {database} on {host}")
        conn.close()
        return True
    except OperationalError as e:
        print(f"❌ FAILED: {e}")
        return False

print("\n=== Testing Connection ===")
test_connection(
    config('DB_HOST', default=''),
    config('DB_NAME', default=''),
    config('DB_USER', default=''),
    config('DB_PASSWORD', default=''),
    config('DB_PORT', default='5432')
)
