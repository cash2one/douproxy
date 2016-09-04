# -*- coding=utf-8 -*-
#copy from iceihehe
#modify
#2016.08.07

class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const{0}".format(name))

        if not name.isupper():
            raise TypeError("Need to bind uppercase")

        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()

import const

const.SUCCESS = 100000
const.NOT_FOUND = 200404
const.TIMEOUT = 200504
const.FORBIDDEN = 200403
const.UNKNOW_ERR = 200999

const.MSG = {
    const.SUCCESS:u'成功了',
    const.NOT_FOUND:u'没找到这个哎',
    const.TIMEOUT:u'请求超时了呀',
    const.FORBIDDEN:u'被屏蔽了呢',
    const.UNKNOW_ERR:u'未知错误'
}

const.PORT = 8001
const.ALLOW_HOST = '127.0.0.1'