# -*- coding: utf-8 -*-

import nexmo
 
client = nexmo.Client(key='2ff54825', secret='bf2a896456351da1')
response = client.send_message(
{
'from': '12033189172',
'to': '14088591938', 
'type': 'unicode',
'text': ' Frpm 大象 Once upon a time, there was a magical Narwhal. Narwhal was the cutest and cuddliest of all Narwhals, and everyone loved this fluffy cutie Narwhal. Narwhal especially loved singing songs with his friendly friend Sheepie. Together they were the cutest and floofiest and squishiest of friends!!!'
})

response = response['messages'][0]

if response['status'] == '0':
  print 'Sent message', response['message-id']
  print 'Remaining balance is', response['remaining-balance']
else:
  print 'Error:', response['error-text']

