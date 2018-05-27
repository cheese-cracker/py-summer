
def git_diff(file1, file2):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            f1 = f1.readlines()
            f2 = f2.readlines()
            jpp = 0
            for j in range(len(f1)):
                flag = 0
                if f1[j] not in f2:
                    print('-'+f1[j][:-1])
                    if j==len(f1)-1:
                        for i in range(jpp, len(f2)):
                            print('+'+f2[i][:-1])
                else:
                    if jpp<len(f2):
                        jp = jpp
                        for i in range(jp, len(f2)):
                            if f1[j] == f2[i]:
                                jpp = i+1
                                break;
                            else:
                                print('+'+f2[i][:-1])
                        if j == len(f1)-1:
                            for i in range(jpp, len(f2)):
                                print('+'+f2[i][:-1])
                    else:
                        print('-'+f1[j][:-1])
