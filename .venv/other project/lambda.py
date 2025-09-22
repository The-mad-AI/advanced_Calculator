names = [ "sara " , "qasem", ' zohre', ' hossein']

short_name = filter(lambda s : len(s)<=6, names)

for name in short_name :    
    print(name)