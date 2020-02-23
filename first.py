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
    # print((library_dict))
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
    with open("ans.txt",'w') as f:
        f.write('90' + '\n')
        # f.write(libraries_str)
        for i in libraries:
            # print((library_dict[i][1]))
            f.write(str(i) + ' '+ str(len(library_dict[i][1]))+ '\n')
            temp_arr_2 = [str(j) for j in library_dict[i][1]]
            temp_str = ' '.join(temp_arr_2)
            f.write(temp_str + '\n')


def sol_b(library_dict):
    data_book = {}
    val_arrs = []
    with open('c_incunabula.txt') as f:
        data = f.readlines()
        # val_arrs = [int(i) for i in data[0].split()]
        temp_arr = [int(i) for i in data[1].split()]
        for i in range(len(temp_arr)):
            data_book[i] = temp_arr[i]
    # B,L,D = val_arrs
    library_dict = readfile('c_incunabula.txt')
    score_save = {}
    for i in range(len(library_dict)):
        temp_val = library_dict[i][1]
        total = 0
        for j in temp_val:
            total += data_book[j]
        score_save[i] = [(total)**4/((library_dict[i][0]))**5]
    sorted_dict = sorted(score_save.items(),key = lambda x: x[1],reverse = True)
    sorted_dict = OrderedDict(sorted_dict)
    # print(type(sorted_dict))
    total_days = 0
    with open('ans2.txt','w') as f:
        f.write('10000'+ '\n')
        for key,val in sorted_dict.items():
            f.write(str(key) + ' ' + str(len(library_dict[key][1]))+ '\n')
            temp_arr_2 = [str(j) for j in library_dict[key][1]]
            temp_str = ' '.join(temp_arr_2)
            f.write(temp_str + '\n')
    

if __name__ == "__main__":
    library_dict = readfile("c_incunabula.txt")
    score_save = sol_b(library_dict)


    