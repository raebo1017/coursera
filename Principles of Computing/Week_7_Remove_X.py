def remove_x(my_string):
	if len(my_string) == 0:
		return ''
	if my_string[0] == 'x':
		return remove_x(my_string[1:])
	else:
		return my_string[0] + remove_x(my_string[1:])
'''
Solution
def remove_x(my_string):
    """
    Takes a string my_string and removes all instances of
    the character 'x' from the string
    Returns a string
    """
    if my_string == "":
        return ""
    else:
        first_character = my_string[0]
        rest_removed = remove_x(my_string[1 :])
        if first_character == 'x':
            return rest_removed
        else:
            return first_character + rest_removed
'''
   
def test_remove_x():
    """
    Some test cases for remove_x
    """
    print "Computed:", "\"" + remove_x("") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("cat") + "\"", "Expected: \"cat\""
    print "Computed:", "\"" + remove_x("xxx") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("dxoxg") + "\"", "Expected: \"dog\""
    
test_remove_x()
print remove_x('xcatxxdogxx')