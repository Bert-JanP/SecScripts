# Example:
# python hash_validator.py d41d8cd98f00b204e9800998ecf8427e
# Outputs:
# Hash algorithm used: MD5

import re
import hashlib
import sys

def validate_hash(hash_value):
    # Convert the hash value to lowercase
    hash_value = hash_value.lower()

    # Regular expressions for hash types
    md5_regex = r'^[0-9a-f]{32}$'
    sha1_regex = r'^[0-9a-f]{40}$'
    sha256_regex = r'^[0-9a-f]{64}$'

    # Check if the hash matches MD5
    if re.match(md5_regex, hash_value):
        return 'MD5'

    # Check if the hash matches SHA1
    if re.match(sha1_regex, hash_value):
        return 'SHA1'

    # Check if the hash matches SHA256
    if re.match(sha256_regex, hash_value):
        return 'SHA256'

    # If none of the hash types match
    return 'Error: Unknown hash algorithm'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python hash_validator.py <hash_value>')
    else:
        hash_value = sys.argv[1]
        algorithm = validate_hash(hash_value)
        print('Hash algorithm used:', algorithm)

