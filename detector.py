import sys

def generate_substrings(l, r):
    l_ret = []
    for i in range(0, len(l)-r+1):
        str = ''
        k = i
        for x in range(0, r):
            str += l[k]
            k += 1
        l_ret.append(str)
    return l_ret

### READ TOKENS
def compare(file1, file2, substring):
    min_size_substring = substring

    print "Reading file 1..."
    with open(file1, 'r') as f1:
        list1 = f1.read().splitlines()
    print "Reading file 2..."
    with open(file2, 'r') as f2:
        list2 = f2.read().splitlines()

    if len(list1) > len(list2):
        list1, list2 = list2, list1

    print "Comparing files..."
    #print "Percent Complete:"
    common = 0
    count_list1_ss = 0
    count_list2_ss = 0
    per1 = 0
    for i in range(0, len(list1)+1):
        per2 = (i * 100 / (len(list1)+1))
        if per2 != per1:
            per1 = per2
            #print per1,
            sys.stdout.write("Current progress: %d%%   \r" % (per1) )
            sys.stdout.flush()

        list1_ss = generate_substrings(list1, i)
        count_list1_ss += len(list1_ss)
        list2_ss = generate_substrings(list2, i)
        count_list2_ss += len(list2_ss)
        for item in list1_ss:
            if item in list2_ss:
                #print item
                common += 1
    sys.stdout.write("Current progress: %d%%   \r" % (100) )
    sys.stdout.flush()

    #print "Common Substrings: ", common
    result = float(common) * 200.0 / (float(count_list1_ss) + float(count_list2_ss))
    print "\n\nResult: " + str(int(result)) + "%"
