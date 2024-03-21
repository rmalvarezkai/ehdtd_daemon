"""
Ehdtd Daemon - auxiliary common function
Common functions used by the package

Author: Ricardo Marcelo Alvarez
Date: 2023-03-14
"""

import os
import urllib.parse
import urllib.request
import json
import zipfile
import io
import time
import datetime
import pprint # pylint: disable=unused-import
import yaml
from schema import Schema, Or

def is_json(myjson):
    """
    is_json
    =======
        This function get a string or bytes and check if json return True
        if the input is a json valid string.
            :param myjson: str | bytes.

            :return bool: Return True if myjson is a str and is a json. 
    """

    result = False

    if myjson is not None and isinstance(myjson,(str,bytes)):
        try:
            json.loads(myjson)
            result = True
        except Exception: # pylint: disable=broad-except
            result = False

    return result

def file_put_contents(filename, data, mode_in=""):
    """
    file_put_contents
    =================
        This function put data into filename
            :param filename: str file path.
            :param data: str
            :param mode: str 'b' for binary mode.

            :return bool: 
    """
    result = False
    mode = "w"

    if len(mode_in) > 0:
        mode = mode_in
    try:
        f = open(filename, mode, encoding='utf-8')
        result = f.write(data)
        f.close()
    except Exception: # pylint: disable=broad-except
        result = False

    return result

def file_get_contents_url(url, mode='b', post_data=None, headers=None, timeout=90):
    """
    file_get_contents_url
    =====================
        This function get a url and reads into a string
            :param url: str file URL.
            :param mode: str 'b' for binary response.
            :param post_data: dict Post data in format key -> value.
            :param headers: dict headers in format key -> value.
            :param timeout: int request timeout.

            :return str: Return response data from url. 
    """

    result = None

    if headers is None:
        headers = {}

    try:
        req = None
        if post_data is not None and isinstance(post_data,dict):
            req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode(), headers)
        else:
            req = urllib.request.Request(url, None, headers)

        if req is not None:
            try:
                with urllib.request.urlopen(req, None, timeout=timeout) as response:
                    result = response.read()


            except Exception: # pylint: disable=broad-except
                result = None

        if mode != 'b' and result is not None and isinstance(result, bytes):
            result = result.decode()

    except Exception: # pylint: disable=broad-except
        result = None

    if mode != 'b' and result is not None and result is not False and isinstance(result, bytes):
        result = result.decode()

    return result

def file_get_contents_url_cmpl(url, mode='b', post_data=None, headers=None, timeout=900):
    """
    file_get_contents_url
    =====================
        This function get a url and reads into a string
            :param url: str file URL.
            :param mode: str 'b' for binary response.
            :param post_data: dict Post data in format key -> value.
            :param headers: dict headers in format key -> value.
            :param timeout: int request timeout.

            :return dict: Return response data from url. 
    """

    result = {}
    result['code'] = None
    result['data'] = None
    result['headers'] = None
    result['headers_str'] = None
    result['final_url'] = None
    result['exception_status'] = False
    result['exception_code'] = None
    result['exception'] = None

    if headers is None:
        headers = {}

    try:
        req = None
        if post_data is not None and isinstance(post_data,dict):
            req = urllib.request.Request(url, urllib.parse.urlencode(post_data).encode(), headers)
        else:
            req = urllib.request.Request(url, None, headers)

        if req is not None:
            try:
                with urllib.request.urlopen(req, None, timeout=timeout) as response:
                    result['code'] = response.status
                    result['data'] = response.read()
                    result['headers'] = response.headers
                    result['headers_str'] = response.headers.as_string()
                    result['final_url'] = response.url

            except Exception as exc: # pylint: disable=broad-except
                result['exception_status'] = True
                if hasattr(exc, 'code'):
                    result['exception_code'] = exc.code
                result['exception'] = exc

        if mode != 'b' and result['data'] is not None and isinstance(result['data'], bytes):
            result['data'] = result['data'].decode()

    except Exception as exc: # pylint: disable=broad-except
        result['exception_status'] = True
        if hasattr(exc, 'code'):
            result['exception_code'] = exc.code
        result['exception'] = exc

    if mode != 'b' and result['data'] is not None\
        and result['data'] is not False\
        and isinstance(result['data'], bytes):
        result['data'] = result['data'].decode()

    return result

def decompress_zip_data(data):
    """
    decompress_zip_data
    ===================
        This function get a url and reads into a string
            :param data: bytes

            :return str: Return decompress data. 
    """

    result = None

    try:
        # z = zipfile.ZipFile(io.BytesIO(data))
        # result = z.read(z.infolist()[0]).decode()

        with zipfile.ZipFile(io.BytesIO(data)) as z:
            result = z.read(z.infolist()[0]).decode()

    except Exception: # pylint: disable=broad-except
        result = None

    return result

def months_ago_counter(from_year, from_month):
    """
    months_ago_counter
    ==================
        This function get a year and month and return months ago
            :param from_year: int
            :param from_month: int

            :return int: months ago
    """

    result = 0

    __this_time = round(time.time())
    __this_year = int(time.strftime("%Y",time.gmtime(__this_time)))
    __this_month = int(time.strftime("%m",time.gmtime(__this_time)))

    date_from = datetime.datetime(from_year, from_month, 1)
    date_to = datetime.datetime(__this_year, __this_month, 1)

    result = (date_to.year - date_from.year) * 12 + date_to.month - date_from.month

    return result

def file_get_contents(filename, mode_in="", encoding='utf-8'):
    """
    file_get_contents
    =================
            :param filename: str
            :param mode_in: str
            :param encoding: str
            :return str:
    """
    result = None
    mode = "r" + mode_in

    try:
        f = open(filename, mode, encoding=encoding)
        result = f.read()
    except Exception: # pylint: disable=broad-except
        result = False

    return result

def read_config_yaml(filename):
    """
    read_config_yaml
    ================
        This function get a year and month and return months ago
            :param filename: str
            :return Any:
    """
    file_raw = file_get_contents(filename)
    res = yaml.safe_load(file_raw)
    return res

def pgrep(pattern):
    """
    pgrep
    =====

    """
    args = "/usr/bin/pgrep" + " -f " + "'" + str(pattern) + "'"
    out = os.popen(args).read().strip()
    return list(map(int, out.splitlines()))

def __check_config_structure(config_data):

    result = False

    schema = Schema({'global': dict,
                     'db_data': dict,
                     'exchanges': dict
                    }
    )

    schema_global = Schema({'log_dir': Or(str, None),
                     'run_dir': Or(str, None),
                     'debug': bool
                    }
    )

    if config_data is not None and schema.is_valid(config_data)\
        and config_data['global'] is not None\
        and schema_global.is_valid(config_data['global']):
        result = True

    return result

def get_config_data(config_file):
    """
    get_config_data
    ===============

    """
    result = None

    config_data = None
    default_config_file = '/etc/ehdtd-daemon/ehdtd-daemon-config.yaml'
    if config_file is not None and isinstance(config_file, str) and os.path.exists(config_file):
        config_data = read_config_yaml(config_file)
    elif os.path.exists(default_config_file):
        config_data = read_config_yaml(default_config_file)

    if __check_config_structure(config_data):
        result = config_data

        if result['global']['log_dir'] is None or not isinstance(result['global']['log_dir'], str):
            result['global']['log_dir'] = '/var/log/ehdtd-daemon'

        if not os.path.exists(result['global']['log_dir']):
            os.makedirs(result['global']['log_dir'])

        if result['global']['run_dir'] is None or not isinstance(result['global']['run_dir'], str):
            result['global']['run_dir'] = '/run'

        if not os.path.exists(result['global']['run_dir']):
            os.makedirs(result['global']['run_dir'])

    return result

def is_pid_running(pid):
    """
    is_pid_running
    ==============

    """
    result = False

    try:
        os.kill(pid, 0)
        result = True
        # print('ENTRE: 0')
    except OSError:
        result = False
        # print('ENTRE: 1')
    else:
        result = True
        # print('ENTRE: 2')

    return result
