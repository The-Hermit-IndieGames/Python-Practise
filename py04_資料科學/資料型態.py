# List -有序、可重複、可變
_List =[1,2,"abc",2]#可以重複
_List.append(1)#添加元素
print("\nList:", _List)

#Set-無序、不重複、可變
_Set={1,2,"abc",2} #自動去重
_Set.add("defg")#添加元素
print("\nSet:", _Set)

# Dictionary-鍵值對,無序但鍵唯一、可變
_Dictionary = {
None:"空",
1:"一",
2:"二"
}

_Dictionary[3]="三"#添加鍵值對
print("\nDictionary:", _Dictionary)

# Tuple-有序、可重複、不可變
_Tuple=(1,2,"abc",2)#可以重複,但內容不可修改
print("\nTuple:", _Tuple)
