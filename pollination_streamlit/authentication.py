import base64
import os
import re
import typing as t

import extra_streamlit_components as stx
import requests
import streamlit as st

COOKIE_NAME = os.getenv('COOKIE_NAME', 'pollination-authz')
PROXY_URL = os.getenv('PROXY_URL', 'http://localhost:8000')


@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()


def _decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


def _decrypt_cookie(cookie: str):
    b64_bytes = _decode_base64(str.encode(cookie))
    parts = b64_bytes.split(b'|')
    value = parts[1]
    token_bytes = _decode_base64(value)
    return token_bytes.decode('utf-8')


def _get_jwt_from_auth_proxy(cookie: str) -> str:
    """Get the logged in user JWT

    Returns:
    str: The base64 encoded user JWT
    """
    res = requests.get(
        f'{PROXY_URL}/auth/jwt',
        cookies={
            COOKIE_NAME: cookie
        }
    )
    res.raise_for_status()
    return res.text


def get_jwt_from_browser() -> t.Optional[str]:
    """Get and decrypt the auth cookie

    Deprecated: this method is not as reliable as the get_jwt method if app auth proxy is v0.5.0 or more

    Returns:
        t.Optional[str]: The decrypted auth cookie if it exists
    """
    cookies = get_manager().get_all()
    cookie = cookies.get(COOKIE_NAME)
    if cookie is None:
        return cookie
    return _decrypt_cookie(cookie)


def get_jwt() -> t.Optional[str]:
    """Get and decrypt the logged in user's JWT

    Returns:
        t.Optional[str]: The decrypted auth cookie if it exists
    """
    cookies = get_manager().get_all()
    cookie = cookies.get(COOKIE_NAME)
    if cookie is None:
        return None
    try:
        return _get_jwt_from_auth_proxy(cookie)
    except requests.HTTPError:
        print(
            "Error fetching JWT from /auth/jwt endpoint. Defaulting to cookie decryption.")
        # Fallback to default cookie decryption technique if not using
        # app-auth-proxy > v0.5.0
        return _decrypt_cookie(cookie)
