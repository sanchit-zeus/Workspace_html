import re

patterns=["term1","term2"]

text ="this is a string with term1, not the other!"

for pattern in patterns:
    print("i'am searching for: "+pattern)

    if re.search(pattern,text):
        print("match")
    else:
        print("no match")

####################################

text="term1"
match=re.search("term1",text)
print(match.start())#matching at zero

########################################

split_term="@"
email="user@gmail.com"
print(re.split(split_term,email))

##########################################

print(re.findall("match","test phrase match in middle"))

#############################################

def mult_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")
test_phrase="sdsd..sssddd..sdddsddd..dsds..dssssss..sddddd"

# test_pattern=["sd+"]
# test_pattern=["sd*"]
# test_pattern=["sd?"]
# test_pattern=["sd{3}"]
# test_pattern=["sd{2,3}"]
test_pattern=["s[sd]+"]
mult_re_find(test_pattern,test_phrase)

#####################################################
def mult_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")
test_phrase="sdsd..sssddd..sdddsddd..dsds..dssssss..sddddd"

# test_pattern=["sd+"]
# test_pattern=["sd*"]
# test_pattern=["sd?"]
# test_pattern=["sd{3}"]
# test_pattern=["sd{2,3}"]
test_pattern=["s[sd]+"]
mult_re_find(test_pattern,test_phrase)

#####################################################
def mult_re_find(patterns,phrase):

    for pat in patterns:
        print("searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")
test_phrase="This is a string with numbers 12312 and a symbol #hashtag"

test_pattern=["[^!.?]+"]
# test_pattern=["[a-z]+"]
# test_pattern=[r"\s+"]#sequence of white space
# test_pattern=[r"\S+"]#sequence of non white space
# test_pattern=[r"\w+"]#sequence of alpha numeric
# test_pattern=[r"\W+"]#sequence of non alpha numeric
# test_pattern=[r"\D+"]#special character code that tell us to search for non digits
# test_pattern=[r"\d+"]#special character code that tell us to search for digits
mult_re_find(test_pattern,test_phrase)
