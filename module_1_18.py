my_dict = {'Bob':1980,'Masha':2000,'Alla':2005}
print('Dict:',my_dict)
print('Existing value:',my_dict['Bob'])
print('Not existing value:',my_dict.get('Peter'))
my_dict['Vasya'] = 1980
my_dict['Shurik'] = 2004
b = my_dict.pop('Bob')
print('Deleted value:',b)
print('Modified dict',my_dict)

my_set = {1,222,222,True,False,'True'}
print('Set:',my_set)
my_set.add(1000)
my_set.add((1,2,3))
my_set.remove(True)

print('Modified set:',my_set)