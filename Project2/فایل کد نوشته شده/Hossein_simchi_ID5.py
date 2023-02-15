import pandas as pd
import math
gp_neg=0
gp_pos=0
ms_neg=0
ms_pos=0
gp = f = u = r =0
ms = m = 0
f_neg = m_neg = f_pos = m_pos = gp_neg = gp_pos = ms_neg = ms_pos = u_neg = u_pos = r_neg = r_pos = 0
entropy = []
entr_s = []
book = pd.read_excel('C:\\Users\\Lenovo\\Desktop\\data.xls')  
book = book.drop(['age'], axis=1)
index = book.index
ncolumns = len(book.columns)
nrows = len (index)
book=book.replace({'Label': r'no'}, {'Label': 0}, regex=True)
book=book.replace({'Label': r'yes'}, {'Label': 1}, regex=True)
Label_pos = Label_neg = None

for i in range(1,26):
    book3 = book.iloc[0:i][:]
    print(book3)
    b = book3["Label"].tolist()
    pos = neg = po = ng = ent_feature1 = ent_feature2 = ent_feature3 = ent_feature4 = 0
    def Features_entropy (feature_name,feature_type,feature_type1,feature_type2,feature_type3):
        entropy1 = entropy2 = entropy3 =entropy4 = entropy_s = neg1 = pos1 = poss = negg = neg2 = pos2 = neg3 = pos3 = 0
        global pos,neg,po,ng,ent_feature1,ent_feature2,ent_feature3,ent_feature4,b
        feature_v = book3[feature_name].tolist()
        w = b + feature_v
        for i in feature_v :
                if i == feature_type:
                    poss += 1
                if i == feature_type1 :
                    negg += 1
                if i == feature_type2 :
                    ng += 1
                if i == feature_type3 :
                    po += 1 
        if poss != 0 :
            entropy_s += -((poss/len(b))*math.log10(poss/len(b)))
            j = len(b)
            for i in range(0,len(b)):
                if w[i]==0 and w[j] == feature_type:
                    neg += 1 
                elif w[i] == 1 and w[j] == feature_type:
                    pos += 1
                j = j + 1
            if neg != 0 :
                entropy1 += -((neg/poss)*math.log10(neg/poss))
            if pos != 0 :
                entropy1 += -((pos/poss)*math.log10(pos/poss))
            ent_feature1=(entropy1)
        if negg != 0 :
            j = len(b)
            entropy_s += -((negg/len(b))*math.log10(negg/len(b)))
            for i in range(0,len(b)):
                if w[i]==0 and w[j] == feature_type1:
                    neg1 += 1 
                elif w[i] == 1 and w[j] == feature_type1:
                    pos1 += 1
                j = j + 1
            if neg1 != 0 :
                entropy2 += -((neg1/negg)*math.log10(neg1/negg))
            if pos1 != 0 :
                entropy2 += -((pos1/negg)*math.log10(pos1/negg))
            ent_feature2=(entropy2)
        if ng != 0 :
            j = len(b)
            entropy_s += -((ng/len(b))*math.log10(ng/len(b)))
            for i in range(0,len(b)):
                if w[i]==0 and w[j] == feature_type2:
                    neg2 += 1 
                elif w[i] == 1 and w[j] == feature_type2:
                    pos2 += 1
                j = j + 1
            if neg2 != 0 :
                entropy3 += -((neg2/ng)*math.log10(neg2/ng))
            if pos2 != 0 :
                entropy3 += -((pos2/ng)*math.log10(pos2/ng))
            ent_feature3=(entropy3)
        if po != 0 :
            entropy_s += -((po/len(b))*math.log10(po/len(b)))
            j =len(b)
            for i in range(0,len(b)):
                if w[i]==0 and w[j] == feature_type3:
                    neg3 += 1 
                elif w[i] == 1 and w[j] == feature_type3:
                    pos3 += 1
                j = j + 1
            if neg3 != 0 :
                entropy4 += -((neg3/po)*math.log10(neg3/po))
            if pos3 != 0 :
                entropy4 += -((pos3/po)*math.log10(pos3/po))
            ent_feature4=(entropy4)
        return pos,neg,ng,po,ent_feature1,ent_feature2,ent_feature3,ent_feature4

    Features = [ 'school' , 'sex' , 'address' , 'famsize' , 'Pstatus' , 'Medu','Fedu' , 'Mjob' , 'Fjob' , 'reason' , 'guardian']
    Features_entropy("school",'GP','MS',None,None)
    ent1 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("sex" , 'F','M',None,None)
    ent2 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("address" , 'U','R',None,None)
    ent3 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("famsize" , 'LE3','GT3',None,None)
    ent4 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("Pstatus" , 'T','A',None,None)
    ent5 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("Medu" , 1,2,3,4)
    ent6 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("Fedu" , 1,2,3,4)
    ent7 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("Mjob" , 'teacher','health','at_home','services')
    ent8 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("Fjob" , 'teacher','health','services','other')
    ent9 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("reason" , 'home','reputation','course','other')
    ent10 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    pos = po = neg = ng = 0
    Features_entropy("guardian" , 'mother','father','other',None)
    ent11 = (pos/len(b))*ent_feature1 + (neg/len(b)) *ent_feature2 + (ng/len(b))*ent_feature3 + (po/len(b))*ent_feature4
    count = 0
    count1 = 0
    for i in b :
        if i == 0 :
            count += 1
        else :
            count1 += 1
    if count1 != 0 and count != 0:
        entropy_s = -((count/len(b))*math.log10(count/len(b)))-((count1/len(b))*math.log10(count1/len(b)))
    elif count != 0 and count1 == 0 :
        entropy_s = -((count/len(b))*math.log10(count/len(b)))
    elif count1 != 0 and count == 0 :
        entropy_s =-((count1/len(b))*math.log10(count1/len(b)))
    t_entropy = []
    tent1 = entropy_s - ent1
    t_entropy.append(tent1)
    tent2 = entropy_s - ent2
    t_entropy.append(tent2)
    tent3 = entropy_s - ent3
    t_entropy.append(tent3)
    tent4 = entropy_s - ent4
    t_entropy.append(tent4)
    tent5 = entropy_s - ent5
    t_entropy.append(tent5)
    tent6 = entropy_s - ent6
    t_entropy.append(tent6)
    tent7 = entropy_s - ent7
    t_entropy.append(tent7)
    tent8 = entropy_s - ent8
    t_entropy.append(tent8)
    tent9 = entropy_s - ent9
    t_entropy.append(tent9)
    tent10 = entropy_s - ent10
    t_entropy.append(tent10)
    tent11 = entropy_s - ent11
    t_entropy.append(tent11)

    from anytree import Node, RenderTree
    attr1=attr2=attr3=attr4=''
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    def count(feature_name,attr1,attr2,attr3,attr4):
        global pos,neg,pos1,neg1,pos2,neg2,pos3,neg3,b
        j = len(b)
        feature_v = book3[feature_name].tolist()
        w = b + feature_v
        for i in range(0,len(b)):
            if w[i]==0 and w[j] == attr1:
                neg += 1 
            elif w[i] == 1 and w[j] == attr1:
                pos += 1
            j = j + 1
        #print("positive attribute1 : {0} and negative attribute1 : {1}".format(pos,neg))
        j = len(b)
        for i in range(0,len(b)):
            if w[i]==0 and w[j] == attr2:
                neg1 += 1 
            elif w[i] == 1 and w[j] == attr2:
                pos1 += 1
            j = j + 1
        j = len(b)
        #print("positive attribute2 : {0} and negative attribute2 : {1}".format(pos1,neg1))
        for i in range(0,len(b)):
            if w[i]==0 and w[j] == attr3:
                neg2 += 1 
            elif w[i] == 1 and w[j] == attr3:
                pos2 += 1
            j = j + 1
        j = len(b)
        #print("positive attribute3 : {0} and negative attribute3 : {1}".format(pos2,neg2))
        for i in range(0,len(b)):
            if w[i]==0 and w[j] == attr4:
                neg3 += 1 
            elif w[i] == 1 and w[j] == attr4:
                pos3 += 1
            j = j + 1
        #print("positive attribute4 : {0} and negative attribute4 : {1}".format(pos3,neg3))
        return pos,neg,pos1,neg1,pos2,neg2,pos3,neg3

    def attribute(Feature_name):
        global attr1,attr2,attr3,attr4
        if Feature_name == "school":
            attr1 = 'GP'
            attr2 = 'MS'
            attr3=attr4 = None
        elif Feature_name == "sex" :
            attr1 = 'F'
            attr2 = 'M'
            attr3=attr4 = None
        elif Feature_name == "address" :
            attr1 = 'U'
            attr2 = 'R'
            attr3=attr4 = None
        elif Feature_name == "famsize" :
            attr1 = 'LE3'
            attr2 = 'GT3'
            attr3=attr4 = None
        elif Feature_name == "Pstatus" :
            attr1 = 'T'
            attr2 = 'A'
            attr3=attr4 = None
        elif Feature_name == "Medu" :
            attr1 = 1
            attr2 = 2
            attr3=3
            attr4 = 4
        elif Feature_name == "Fedu" :
            attr1 = 1
            attr2 = 2
            attr3=3
            attr4 = 4
        elif Feature_name == "Mjob" :
            attr1 = 'teacher'
            attr2 = 'health'
            attr3= 'other'
            attr4 = 'services'
        elif Feature_name == "Fjob" :
            attr1 = 'teacher'
            attr2 = 'health'
            attr3= 'services'
            attr4 = 'other'
        elif Feature_name == "reason" : 
            attr1 = 'home'
            attr2 = 'reputation'
            attr3= 'course'
            attr4 = 'other'
        elif Feature_name == "guardian" : 
            attr1 = 'mother'
            attr2 = 'father'
            attr3= 'other'
            attr4 = None
        return Feature_name , attr1 , attr2 , attr3 , attr4
    r = 1
    def pos_neg(t,attr1,attr2,attr3,attr4):
        c = 0
        global r
        if pos==0 or neg == 0 :
            if pos != 0 :
                sec_node = Node (str(attr1) + "+", parent = t)
                c = c + 1
            elif neg != 0 :
                sec_node = Node (str(attr1) + "-", parent = t)
                c = c + 1           
        if pos1 == 0 or neg1 == 0 :
            if pos1 != 0 :
                the_node = Node (str(attr2) + "+", parent = t)
                c = c + 1
            elif neg1 != 0 :
                the_node = Node (str(attr2) + "-" , parent = t)
                c = c + 1
        if pos2==0 or neg2 == 0 :
            if pos2 != 0 :
                uh_node = Node (str(attr3) + "+", parent = t)
                c = c + 1
            elif neg2 != 0 :
                uh_node = Node (str(attr3) + "-" , parent =t)
                c = c + 1
        if pos3==0 or neg3 == 0 :
            if pos3 != 0 :
                for_node = Node (str(attr4) + "+", parent = t)
                c = c + 1
            elif neg3 != 0 :
                for_node = Node (str(attr4) + "-", parent = t)
                c = c + 1
        if c >= 2 :
            r = 2
        return r

    p = []       
    index = t_entropy.index(max(t_entropy))
    root = Features[index]
    root = str(root)
    first_node = Node (root)
    Feature_name = root
    attribute(Feature_name)
    count(Feature_name,attr1,attr2,attr3,attr4)
    pos_neg(first_node,attr1,attr2,attr3,attr4)
    #pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr5,attr6,attr7,attr8=attr1,attr2,attr3,attr4
    a = 0
    p.append(a)
    #--------------------------------------------------------------------------------------------
    t_entropy.remove(max(t_entropy))
    t_entropy1 = t_entropy
    Features.remove(root)
    Features1 = Features
    index1 = t_entropy.index(max(t_entropy))
    node1 = Features1 [index1]
    node1= str (node1)
    second_node = Node(node1)
    if r == 2 :
        second_node = Node(node1)
        a = 1
        p.append(a)
    else :
        second_node = Node(node1,parent = first_node)
    r = 1
    Feature_name1 = node1
    attribute(Feature_name1)
    count(Feature_name1,attr1,attr2,attr3,attr4)
    pos_neg(second_node,attr1,attr2,attr3,attr4)
    #_________________________________________________________

    t_entropy1.remove(max(t_entropy1))
    t_entropy2 = t_entropy1
    Features1.remove(node1)
    Features2 = Features1
    index2 = t_entropy2.index(max(t_entropy2))
    node2 = Features2 [index2]
    node2 = str (node2)
    if r == 2 :
        third_node = Node(node2)
        a =2 
        p.append(a)
    else :
        third_node = Node(node2,parent=second_node)
    r = 1
    Feature_name2 = node2
    attribute(Feature_name2)
    count(Feature_name2,attr1,attr2,attr3,attr4)
    pos_neg(third_node,attr1,attr2,attr3,attr4)


    #------------------------------------------------------------------

    t_entropy2.remove(max(t_entropy2))
    t_entropy3 = t_entropy2
    Features2.remove(node2)
    Features3 = Features2
    index3 = t_entropy3.index(max(t_entropy3))
    node3 = Features3 [index3]
    node3 = str (node3)
    if r == 2 :
        forth_node = Node(node3)
        a = 3
        p.append(a)
    else :
        forth_node = Node(node3,parent=third_node)
    r = 1
    Feature_name3 = node3
    attribute(Feature_name3)
    count(Feature_name3,attr1,attr2,attr3,attr4)
    pos_neg(forth_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #-------------------------------------------
    t_entropy3.remove(max(t_entropy3))
    t_entropy4 = t_entropy3
    Features3.remove(node3)
    Features4 = Features3
    index4 = t_entropy4.index(max(t_entropy4))
    node4 = Features4 [index4]
    node4 = str (node4)
    if r == 2 :
        fifth_node = Node(node4)
        a = 4
        p.append(a)

    else :
        fifth_node = Node(node4,parent=forth_node)
    r = 1
    Feature_name4 = node4
    attribute(Feature_name4)
    count(Feature_name4,attr1,attr2,attr3,attr4)
    pos_neg(fifth_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #----------------------------------------------------
    t_entropy4.remove(max(t_entropy4))
    t_entropy5 = t_entropy4
    Features4.remove(node4)
    Features5 = Features4
    index5 = t_entropy5.index(max(t_entropy5))
    node5 = Features5 [index5]
    node5 = str (node5)
    if r == 2 :
        six_node = Node(node5)
        a = 5
        p.append(a)
    else :
        six_node = Node(node5,parent = fifth_node)
    r = 1
    Feature_name5 = node5
    attribute(Feature_name5)
    count(Feature_name5,attr1,attr2,attr3,attr4)
    pos_neg(six_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #-----------------------------------------------------------
    t_entropy5.remove(max(t_entropy5))
    t_entropy6 = t_entropy5
    Features5.remove(node5)
    Features6 = Features5
    index6 = t_entropy6.index(max(t_entropy6))
    node6 = Features6 [index6]
    node6 = str (node6)
    if r == 2 :
        seven_node = Node(node6)
        a = 6
        p.append(a)
    else :
        seven_node = Node(node6,parent = six_node)
    r = 1
    Feature_name6 = node6
    attribute(Feature_name6)
    count(Feature_name6,attr1,attr2,attr3,attr4)
    pos_neg(seven_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #-----------------------------------------------------------
    t_entropy6.remove(max(t_entropy6))
    t_entropy7 = t_entropy6
    Features6.remove(node6)
    Features7 = Features6
    index7 = t_entropy7.index(max(t_entropy7))
    node7 = Features7 [index7]
    node7 = str (node7)
    if r == 2 :
        eight_node = Node(node7)
        a = 7
        p.append(a)
    else :
        eight_node = Node(node7,parent = seven_node)
    r = 1
    Feature_name7 = node7
    attribute(Feature_name7)
    count(Feature_name7,attr1,attr2,attr3,attr4)
    pos_neg(eight_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #-----------------------------------------------
    t_entropy7.remove(max(t_entropy7))
    t_entropy8 = t_entropy7
    Features7.remove(node7)
    Features8 = Features7
    index8 = t_entropy8.index(max(t_entropy8))
    node8 = Features8 [index8]
    node8 = str (node8)
    if r == 2 :
        nine_node = Node(node8)
        a = 8
        p.append(a)
    else :
        nine_node = Node(node8,parent = eight_node)
    r = 1
    Feature_name8 = node8
    attribute(Feature_name8)
    count(Feature_name8,attr1,attr2,attr3,attr4)
    pos_neg(nine_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #-----------------------------------------------------
    t_entropy8.remove(max(t_entropy8))
    t_entropy9 = t_entropy8
    Features8.remove(node8)
    Features9 = Features8
    index9 = t_entropy9.index(max(t_entropy9))
    node9 = Features9 [index9]
    node9 = str (node9)
    if r == 2 :
        ten_node = Node(node9)
        a = 9
        p.append(a)
    else :
        ten_node = Node(node9,parent = nine_node)
    r = 1
    Feature_name9 = node9
    attribute(Feature_name9)
    count(Feature_name9,attr1,attr2,attr3,attr4)
    pos_neg(ten_node,attr1,attr2,attr3,attr4)
    pos=neg=pos1=neg1=pos2=neg2=pos3=neg3=0
    attr1=attr2=attr3=attr4=''
    #---------------------------------------------------------
    t_entropy9.remove(max(t_entropy9))
    t_entropy10 = t_entropy9
    Features9.remove(node9)
    Features10 = Features9
    index10 = t_entropy10.index(max(t_entropy10))
    node10 = Features10 [index10]
    node10 = str (node10)
    if r == 2 :
        eleven_node = Node(node10)
        a = 10 
        p.append(a)
    else :
        eleven_node = Node(node10,parent = ten_node)
    r = 1
    Feature_name10 = node10
    attribute(Feature_name10)
    count(Feature_name10,attr1,attr2,attr3,attr4)
    if attr1 != None :
        if pos == 0 or neg == 0 :
            n = str(attr1)
            n1 = Node(n , parent = eleven_node)
            if pos != 0 :
                node13 = Node(str(attr1) + "+",parent = n1)
            if neg != 0 :
                node14= Node(str(attr1) + "-",parent = n1)
    if attr2 != None :
        if pos1 == 0 or neg1 == 0 :
            n = str (attr2)
            n1 = Node (n , parent = eleven_node)
            if pos1 != 0 :
                node15 = Node(str(attr2) + "+",parent = n1)
            if neg1 != 0 :
                node16 = Node(str(attr2) + "-",parent = n1)
    if attr3 != None :
        if neg2 == 0 or pos2 == 0 :
            n = str (attr3)
            n1 = Node (n , parent = eleven_node)
            if pos2 != 0 :
                node15 = Node(str(attr3) + "+",parent = n1)
            if neg2 != 0 :
                node16 = Node(str(attr3) + "-",parent = n1)
    if attr4 != None :
        if pos3 == 0 or neg3 == 0 :
            n = str (attr4)
            n1 = Node (n , parent = eleven_node)
            if pos3 != 0 :
                node15 = Node(str(attr4) + "+",parent = n1)
            if neg3 != 0 :
                node16 = Node(str(attr4) + "-",parent = n1)
    li = [first_node,second_node,third_node,forth_node,fifth_node,six_node,seven_node,eight_node,nine_node,ten_node,eleven_node]
    for i in range(len(p)):
        for pre, fill, node in RenderTree(li[p[i]]):
            print("%s%s" % (pre, node.name))
        
TP=FP=FN=TN=0
def precision():
    global Label_pos,Label_neg,TP,FP,FN,TN
    count_pos = count_neg = 0
    book1 = book.iloc[0:26][:]
    b = book1["Label"].tolist()
    for i in b :
        if i == 1 :
            count_pos += 1
        else :
            count_neg += 1
    if count_pos > count_neg :
        Label_pos = 1
    else :
        Label_neg = 0
    book1 = book.iloc[36:55][:]
    b1 = book1["Label"].tolist()
    for t in range(len(b1)):
        if b1[t] == 1 and Label_pos == 1 :
            TP += 1
        elif b1[t] == 1 and Label_neg == 0: 
            FN += 1
        elif b1[t] == 0 and Label_pos == 1:
            FP += 1
        elif b1[t] == 0 and Label_neg == 0 :
            TN += 1
    return TP,FP,FN,TN
precision()
if Label_pos ==1:
    precision = TP/(TP + FP)
    print("The prcision on test data is {0}".format(precision))
elif Label_neg == 0 :
    precision = TN/(TN + FN)
    print("The prcision on test data is {0}".format(precision))
            
                
