#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat, time, re
from itchat.content import *
from random import choice

def getRandomBlessing ():
  blessingList = u'新年快乐-鸡年期盼你：天天开心!-祝君年年旺，团团又圆圆-祝鸡年心怡，鸡年大吉-越长越美😄-恭喜发大财'.split('-')  
  return choice(blessingList)

@itchat.msg_register([TEXT])
def text_reply(msg):
    isMatch = re.search(u'year|年', msg['Text'], re.IGNORECASE).span() 
    if isMatch:
      blessing = getRandomBlessing()
      print 'start reply: ' + blessing
      itchat.send(blessing, msg['FromUserName'])

itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()

