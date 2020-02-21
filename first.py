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
    sorted_dict = {k: v for k, v in sorted(library_dict.items(), key=lambda item: item[1][0])}
    return sorted_dict


if __name__ == "__main__":
    library_dict = readfile("b_read_on.txt")
    f = sol_a(library_dict)
    print((f[1]))



    