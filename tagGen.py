from yantran import Yantranslator

from_lang='en' #language of titles
to_lang='hi' #keywords should also be translated into


translator = Yantranslator('ENTER_YOUR_FREE_API_KEY_HERE')

fs = ""
fi =open('keywords.txt','w+',encoding = 'utf-8')
with open('titles.txt') as f:
	lines = f.readlines()
count =0

for string in lines:
	bow = string.split(" ")
	final=[]
	final_string = ""
	for w in bow:
		if(w=='and'):
			continue
		elif(w[-1:]=="s"):
			final.append(w[:-1].lower())
		elif(w[-2:]=="es"):
			final.append(w[:-2].lower())
		else:
			final.append(w.lower())
	for f in final:
		trans = translator.tran_sentence('en','hi',f)
		trans = trans.replace('\n','')
		if(len(trans.split())>1):
			continue
		final_string = final_string+trans+', '
	for x in final:
		final_string=final_string+x+', '
	fs=fs+final_string[:-2]
fi.write(fs)
