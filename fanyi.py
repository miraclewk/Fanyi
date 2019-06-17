###################翻译###########################
import requests
#import json
from google import Py4Js 
# from baidu import findsign 
# import js2py
# import re
ydheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','x-requested-with':'XMLHttpRequest',
	'Referer':'http://fanyi.youdao.com/?keyfrom=dict2.index'
}
bdheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest',
	'Referer':'http://fanyi.baidu.com/','Host':'fanyi.baidu.com'
}
ggheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'referer':'https://translate.google.cn/'
}
oluheaders={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
headers_h = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
url_youdao='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
url_phone= 'http://fanyi.baidu.com/basetrans'
url_baidu='http://fanyi.baidu.com/transapi'
url_olu='http://dict.eudic.net/Home/TranslationAjax'
js = Py4Js() 
def baidu_phone(content):
    detect_url = 'http://fanyi.baidu.com/langdetect'
    set_data = {'query': content}
    response = requests.post(detect_url, headers=headers_h, data=set_data)
    detect_json = response.content.decode()
    detect = json.loads(detect_json)['lan']
    to = 'zh' if detect =='en' else 'en'
    search_data = {'query': content,
                    'from': detect,
                    'to': to}
    response = requests.post(url_phone, headers=headers_h, data=search_data).content.decode()
    data_dict = json.loads(response)
    fanyi_bai = data_dict['trans'][0]['dst']
    print('百度翻译：',fanyi_bai+'\n')

def olu(content):
    data={'to':'zh-CN','from':'en','text':content}
    response=requests.post(url_olu,data=data,headers=oluheaders)
    baidu_result=response.text
    print('\n欧路词典：',baidu_result)

def youdao(content):
	data={
		'i':content,
		'from':'AUTO',
		'to':'AUTO',
		'smartresult':'dict',
		'client':'fanyideskweb',
		'salt':'1533907163550',
		'sign':'e8fb6c81be653475e67a42f06ee7c679',
		'doctype':'json',
		'version':'2.1',
		'keyfrom':'fanyi.web',
		'action':'FY_BY_CLICKBUTTION',
		'typoResult':'false'
	}
	response=requests.post(url_youdao,data=data,headers=ydheaders)
	result=response.json()
	length=len(result['translateResult'][0])
	fanyi_result=''
	for i in range(length):
		fanyi_result=fanyi_result+result['translateResult'][0][i]['tgt']#+'。'
	print('\n有道翻译：',fanyi_result+'\n')

def baidu(content):
#	sign=findsign(content)
#	data={'from':'en','to':'zh','query':content,'transtype':'translang','simple_means_flag':'3','sign':sign,'token':'d3e57e8f690ef485d54ee9dd68e0da30'}
	data={'from':'en','to':'zh','query':content}
	response=requests.post(url_baidu,data=data,headers=bdheaders)
	baidu_result=response.json()
	print(baidu_result)
 #   print('百度翻译：',baidu_result['data'][0]['dst']+'\n')
def baiducn(content):
	data={'from':'zh','to':'en','query':content}
	response=requests.post(url_baidu,data=data,headers=bdheaders)
	baidu_result=response.json()
	print('百度翻译：',baidu_result['data'][0]['dst']+'\n')

def google(content): 
	tk = js.getTk(content)     
	param = {'tk': tk, 'q': content}
	result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
		&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
		&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=6&kc=0""", params=param,headers=ggheaders)
	fanyi_ans=result.json()
	length=len(fanyi_ans[0])
	fanyi_answer=''
	for i in range(length-1):
		fanyi_answer=fanyi_answer+fanyi_ans[0][i][0]
	# if content==fanyi_answer:
	# 	result1 = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=zh-CN
	# 		&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
	# 		&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=3&kc=0""", params=param,headers=ggheaders)
	# 	fanyi_ans=result1.json()
	# 	length=len(fanyi_ans[0])
	# 	fanyi_answer=''
	# 	for i in range(length-1):
	# 		fanyi_answer=fanyi_answer+fanyi_ans[0][i][0]
	print('谷歌翻译：',fanyi_answer+'\n')
def googlecn(content):
	tk = js.getTk(content)     
	param = {'tk': tk, 'q': content}
	result1 = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=zh-CN
	 		&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
	 		&dt=t&ie=UTF-8&oe=UTF-8&source=btn&ssel=3&tsel=3&kc=0""", params=param,headers=ggheaders)
	fanyi_ans=result1.json()
	length=len(fanyi_ans[0])
	fanyi_answer=''
	for i in range(length-1):
		fanyi_answer=fanyi_answer+fanyi_ans[0][i][0]
	print('谷歌翻译：',fanyi_answer+'\n')

if __name__ == '__main__':
	# while True:
	# 		content=input('\n\n请输入要翻译的内容/输入ex退出：')
	# 		if content=='ex':
	# 			break
	# 		else:
	# #			baidu_phone(content)
	# 			youdao(content)
	# 			baidu(content)
	# 			google(content)
	print('8.13更新内容：\n1、修复了翻译语言中碰到句号不再翻译后面语句的bug\n2、修复了百度翻译一旦过长就报错的bug\n3、修复了不能直接复制文本进行翻译的bug\n4、更多更新尽请期待\n')
	while True:
		choice=input('\n请选择语言，英译中输入en/中译英输入cn/退出输入q：')
		if choice=='q':
			break
		elif choice=='en':
			while True:
				print('\n\n请输入要翻译的内容/输入ex退出当前模式：')
				print('注意：由于没有制作GUI,考虑到复制的文本太长会让系统在换行的时候默认执行\n所以请在输入完毕按下enter后输入e结束此次输入\n')
				lines = []
				for line in iter(input, 'e'):
					lines.append(line)
				content=' '.join(lines)
				if content=='ex':
					break
				else:
		#			baidu_phone(content)s
					olu(content)
					youdao(content)
			#		baidu(content)
					google(content)
		elif choice=='cn':
			while True:
				print('\n\n请输入要翻译的内容/输入ex退出当前模式：')
				print('注意：由于没有制作GUI,考虑到复制的文本太长会让系统在换行的时候默认执行\n所以请在输入完毕按下enter后输入e结束此次输入\n')
				lines = []
				for line in iter(input, 'e'):
					lines.append(line)
				content=' '.join(lines)
				if content=='ex':
					break
				else:
		#			baidu_phone(content)
					youdao(content)
			#		baiducn(content)
					googlecn(content)
		else:
			print('输入错误')
# ###############################################################
#1/谷歌翻译不能中译英    搞定√
#2/可以考虑多进程
#3/复制过来的文本一旦有两行及以上，他就会分开执行 搞定√
#4/不具备移植性 搞定√
#5/设计一个gui
#6/百度翻译不能翻译太长 搞定√
#7/不能有句号，也不是说不上原因 搞定√
#8/有道翻译不能有句号 搞定√
#9/百度翻译不能智能识别中英文 搞定√
#10/谷歌翻译中译英会翻译成繁体字bug
