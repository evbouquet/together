# -*- coding: utf-8 -*-

import nexmo
 
client = nexmo.Client(key='2ff54825', secret='bf2a896456351da1')
response = client.send_message(
{

 'from': '12033189172',
# US number
 'to': '14088591938',
# China number
# 'to': '8613161503275',

'type': 'unicode',
#'text': 'Would you want to be a billonaire in your lifetime? Call this number and find out how.'
'text': '明月如霜，好风如水，清景无限。曲港跳鱼，圆荷泻露，寂寞无人见。紞如三鼓，铿然一叶，黯黯梦云惊断。夜茫茫，重寻无处，觉来小园行遍。天涯倦客，山中归路，望断故园心眼。燕子楼空，佳人何在，空锁楼中燕。古今如梦，何曾梦觉，但有旧欢新怨。异时对，黄楼夜景，为余浩叹。'
})

response = response['messages'][0]

if response['status'] == '0':
  print ('Sent message', response['message-id'])
  print ('Remaining balance is', response['remaining-balance'])
else:
  print ('Error:', response['error-text'])

