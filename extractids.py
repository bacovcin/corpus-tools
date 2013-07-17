import string

ids = []
afile = open('oldeng_external.c')
for line in afile:
    if 'ID' in line:
	ids.append(line.split(':')[0].lstrip().rstrip())
outfile = open('OEdata.txt','w')
outfile.write('TextName:Lat,Long,Location,Dialect,Genre,YoC,YoM,AuthName,AuthBD,AuthSex,AuthAge,RecName,RecBD,RecSex,RecAge,RecRelation,Words,OCWords,NamWords,ForWords,Types,OCTypes,NamTypes,ForTypes,Chars,OCChars,NamChars,ForChars,Tokens\n')
for item in ids:
    outfile.write(item + ':x,x,x,x,x,x,x,x,xxxx,x,xx,x,xxxx,x,xx,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n')
