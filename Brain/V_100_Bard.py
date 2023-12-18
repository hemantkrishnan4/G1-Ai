from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "dwhtB3mzw3cHXZdgOkwIK3YLSFZ5D_Z2A29PxTLJt_erYmPwtFrqUcypuGe8DXEZqGaaOQ.",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSiVrAtAVBi3FkjqZfG7K-QS5lQoIKKZICnc-qMTlN-6SXOWZ5v9JUIn6eHjfEAA",
    "__Secure-1PSIDCC": "ABTWhQHzo2SBEYmGiEqYMBPFL8G97feNr-S3K5cXyoouub31bMVBoIENnKy0UaIOMMnKMFAn0-mo",
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    query = input("Enter Your Query:")
    reply = bard.get_answer(query)["content"]
    print(reply)
