#coding:utf-8

import os
import sys

import logging

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


#配置

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',           #line 为行号
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')

# 模块级别的函数

logger = logging.getLogger()

#创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 在撞见一个handler，输出到控制台
ch = logging.StremHandler()

formatter = logging.Formater('')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)


# 应用  银行卡消费记录
def get_logger(card_num, struct_time):

    if struct_time.tm_mday < 23:
        file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon, 22)
    else:
        file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon+1, 22)

    file_handler = logging.FileHandler(
        os.path.join(settings.USER_DIR_FOLDER, card_num, 'record', file_name),
        encoding='utf-8'
    )
    fmt = logging.Formatter(fmt="%(asctime)s :  %(message)s")
    file_handler.setFormatter(fmt)

    logger1 = logging.Logger('user_logger', level=logging.INFO)
    logger1.addHandler(file_handler)
    return logger1

#调用
logger = get_logger()
logger.info('spend &s $'% '999' )













