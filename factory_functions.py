def make_bread(arg1, arg2, arg3):
    if arg1 == 'water' and arg2 == 'flour' and arg3 == 'eggs':
        return 'dough'
    else:
        return 'not dough'

# Test for bake
def bake(arg1):
    if arg1 == 'dough':
        return 'brioche'
    else:
        return 'not brioche'

def run_factory(arg1, arg2, arg3):
    result_dough = make_bread(arg1, arg2, arg3)
    result_bake = bake(result_dough)
    return result_bake
# Tests for make bread

# print('Testing make dough() with water, flour and eggs. Expected dough')
# # # print(make_bread('water', 'flour', 'eggs') == 'dough')

#simple unit test
print('Testing make dough() with water, cement and gravel. dough')
print(make_bread('water', 'cement', 'gravel') == 'dough')


print(('testing bake() concrete. expected brioche'))
print(bake('concrete') == 'brioche')

## simple integration test
print('testing run_factory() with water flour and eggs. Expected brioche')
print(run_factory('cement', 'flour', 'eggs') == 'not brioche')