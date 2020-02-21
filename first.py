from collections import defaultdict,OrderedDict
def readfile(filename):
    library_dict = {}
    with open(filename,'r') as f:
        data = f.readlines()
        # print(type(data[0]))
        B,L,D = data[0].split()
        for i in range(1,int(len(data)/2)):
            temp_arr = [int(i) for i in data[2*i].split()]
            c = temp_arr[1]
            val_books = [int(i) for i in data[2*i+1].split()]
            library_dict[i-1] = [c,val_books]
    # print((library_dict)[2])
    return library_dict 


def sol_a(library_dict):
    # sorted_dict = {k: v for k, v in sorted(library_dict.items(), key=lambda item: item[1][0])}
    sorted_dict = sorted(library_dict.items(),key = lambda x: x[1][0])
    # print(sorted_dict[i][0])
    libraries = []
    # libraries = [i[0] for i in sorted_dict]
    # days  = [i[1][0] for i in sorted_dict]
    # print(libraries)
    total = 0
    for i in sorted_dict:
        total += i[1][0]
        if total >= 1000:
            break
        libraries.append(i[0])
    # str_x = ' '.join(str(library_dict[0][1]))
    # print(str_x)
    with open("ans.txt",'w') as f:
        f.write('90' + '\n')
        # f.write(libraries_str)
        for i in libraries:
            # print((library_dict[i][1]))
            f.write(str(i) + ' '+ str(len(library_dict[i][1]))+ '\n')
            temp_arr_2 = [str(j) for j in library_dict[i][1]]
            temp_str = ' '.join(temp_arr_2)
            f.write(temp_str + '\n')


if __name__ == "__main__":
    library_dict = readfile("b_read_on.txt")
    f = sol_a(library_dict)
    # print((f[1]))



    