calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    string = len(string), string.upper(), string.lower()
    return string

def is_contains(string,list_to_search):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))
print(is_contains('cycle',['recycling','cyclic']))
print(calls)