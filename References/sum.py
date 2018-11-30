
def show(request,string):
    # print()
    sent=[]
    textsent = []
    matchsent = []
    fulllist = []


    print(string)
    d1 = io.open('%s.txt'%string,'r', encoding="utf-8")
    text = d1.read()
    text =  re.sub('[!@#$\n\t0123456789]','',text)
    text=text.replace("'","")
    text = text.replace("(","")
    text = text.replace(")","")
    text = text.replace("-","")
    text = text.replace("_","")
    text = text.replace('"','')
    text = text.replace('[','')
    text = text.replace(']','')
    text = text.replace('^','')
    text = text.replace('?','')
    text = text.replace('*','')
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text)
    for senten in m:
        textsent.append(senten)
    d1.close()
    d1 = io.open('sentences.txt','r', encoding="utf-8")
    file1_data = d1.read()
    file1_data =  re.sub('[!@#$\n\t0123456789-]','',file1_data)
    file1_data=file1_data.replace("'","")
    file1_data=file1_data.replace("(","")
    file1_data=file1_data.replace(")","")
    file1_data=file1_data.replace("-","")
    file1_data=file1_data.replace("_","")
    file1_data=file1_data.replace('"','')
    file1_data=file1_data.replace('[','')
    file1_data=file1_data.replace(']','')
    file1_data=file1_data.replace('^','')
    file1_data=file1_data.replace('?','')
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', file1_data)
    for senten in m:
        sent.append(senten)
    d1.close()
    print(len(sent))
    for se in sent:
        # print(se)
        gg = difflib.get_close_matches(se[:30],textsent,n=4,cutoff=0.3)
        matchsent.append(gg)

    for se in matchsent:
        for s in se:
            fulllist.append(s)
    print(fulllist)
    json_list = json.dumps(fulllist)





    return render(request,'show.html',{'text':text,'sentences':json_list,})
