# -*- coding: utf-8 -*-

import nexmo
 
client = nexmo.Client(key='2ff54825', secret='bf2a896456351da1')
response = client.send_message(
{
#'from': '12033189172',
#'to': '14088591938', 
#'type': 'unicode',
#'text': ' From 大象 Once upon a time, there was a magical Narwhal. Narwhal was the cutest and cuddliest of all Narwhals, and everyone loved this fluffy cutie Narwhal. Narwhal especially loved singing songs with his friendly friend Sheepie. Together they were the cutest and floofiest and squishiest of friends!!!'
'from': 'Zshiled',
'to': '8613161503275',
'type': 'unicode',
'text': '怅卧新春白袷衣，白门寥落意多违。红楼隔雨相望冷，珠箔飘灯独自归。远路应悲春晚晚，残宵犹得梦依稀。玉珰缄札何由达，万里云罗一雁飞。君不见，黄河之水天上来，奔流到海不复回。君不见，高堂明镜悲白发，朝如青丝暮成雪！人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马、千金裘，呼儿将出换美酒，与尔同销万古愁！'
})

response = response['messages'][0]

if response['status'] == '0':
  print 'Sent message', response['message-id']
  print 'Remaining balance is', response['remaining-balance']
else:
  print 'Error:', response['error-text']

