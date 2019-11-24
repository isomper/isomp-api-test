
import time
import base64

def sleep(n_secs):
    time.sleep(n_secs)

#base64给密码加密
def base64_encode(pwd):
    bs64_pwd = base64.b64encode(pwd.encode('utf-8'))
    print(bs64_pwd)

    return bs64_pwd


def hook_print(str):
    print("********" + str + " print********")


def get_pwd():
    return [
        {'pwd':'admin'},
	{'pwd':'a123'}
         
    ]

def get_userName_passWord():
    return [
        {'userName':'admin', 'passWord':'admin'},
        {'userName':'a123', 'passWord':'123'}

    ]


#if __name__ == "__main__":
#    base64_pwd = base64_encode('admin')
