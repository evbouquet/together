# -*- coding: utf-8 -*-

import nexmo
 
client = nexmo.Client(key='2ff54825', secret='bf2a896456351da1')
response = client.send_message(
{
'from': '12033189172',
'to': '14088591938', 
'text': 'Hello 大翔 from Zshield'
})

response = response['messages'][0]

if response['status'] == '0':
  print 'Sent message', response['message-id']

  print 'Remaining balance is', response['remaining-balance']
else:
  print 'Error:', response['error-text']

