

list1=[1,2,3,4]

list2=["apple","banana","orange","kiwi", "mango"]

newlist_a=[]
newlist_without_a=[]
newlist2=[]

def a_in_word_append_list():

  for list in list2 :

    if "a" in list:

        newlist_a.append(list)

        print(newlist_a)


def a_notin_word_append_list():

  for list in list2 :

    if "a" in list:
        continue
    else:
        newlist_without_a.append(list)


        print(newlist_without_a)

def listvalues_list1():
            
     [print(x ) for x in list1 ]

def length_of_list():
      

    print(f'Length of {list1} is:', len(list1))

    print(f'Length of {list2} is:', len(list2))





a_in_word_append_list()

a_notin_word_append_list()

listvalues_list1()

length_of_list()


