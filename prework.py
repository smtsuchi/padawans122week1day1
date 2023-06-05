def is_consecutive(a_list):
    status = ""
    True
    for index in range( len(a_list)-1 ):
        if a_list[index] + 1 == a_list[index + 1]:
            'do nothing'
        else:
            status = False
            break

    print(status)


is_consecutive([11,12, 13,14,15,16,17,18,19,20])

# question 2
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)
    # questrion 3
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)