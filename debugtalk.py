# -*- coding: utf-8 -*-
import hashlib
import hmac
import random
import json
import string
import base64
import hashlib
import os

SECRET_KEY = "DebugTalk"
# os.environ['http_proxy'] = 'http://127.0.0.1:8080'
# os.environ['https_proxy'] = 'https://127.0.0.1:8080'

def setup_print():
	print("---------------------setup hook is ok---------------------")


def teardown_print():
	print("---------------------teardown hooks is ok------------------")


def gen_random_string(str_len):
    """ generate random string with specified length
    """
    return ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(str_len))

def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign

def gen_md5(*args):
    return hashlib.md5("".join(args).encode('utf-8')).hexdigest()


#base64给密码加密
def base64_encode(pwd):
    bs64_pwd = base64.b64encode(pwd.encode('utf-8'))
    print(bs64_pwd)

    return bs64_pwd

#生成随机数
def get_random():
    random_num = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',4))

    return random_num

#md5加密
def md5_encode(md5_random):
    md5_obj = hashlib.md5()

    md5_obj.update(md5_random)

    return md5_obj.hexdigest()

#返回md5值和随机数
def get_md5_value(random_num):

    md5_val = (salt + random_num).encode('utf-8')

    md5_value = md5_encode(md5_val)
    print (md5_val)

    return  md5_value

# 读取文件内容
def get_file(filePath):
    return open(filePath, "rb")


if __name__ == "__main__":
    #base64_pwd = base64_encode('admin')
    random_num = get_random()
    print (random_num)
    print (get_md5_value(random_num))