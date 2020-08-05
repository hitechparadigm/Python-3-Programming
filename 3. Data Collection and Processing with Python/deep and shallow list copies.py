# deep and shallow list copies
import copy
original = ['1', '2', ['3', '4'], ['5', '6'], 'hello', ['cat', 'dog'], 'this is some info']
alias_original = original
shallow_copy = original[:]
deep_copy = copy.deepcopy(original)
print (".... initial versions of the lists ....")
print("original list ID: {}".format(id(original)))
print(original)

print("alias ID: {}".format(id(alias_original)))
print(alias_original)

print("shallow copy ID: {}".format(id(shallow_copy)))
print(shallow_copy)

print("deep copy ID: {}".format(id(deep_copy)))
print(deep_copy)

# changing the orginal list

original[2].append('New First!')
original.append('Hello There!')
alias_original[3].append("Replacement of 4th element")
print(".... after update ....")
print("original list ID: {}".format(id(original)))
print(original)

print("alias ID: {}".format(id(alias_original)))
print(alias_original)

print("shallow copy ID: {}".format(id(shallow_copy)))
print(shallow_copy)

print("deep copy ID: {}".format(id(deep_copy)))
print(deep_copy)
