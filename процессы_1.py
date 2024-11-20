import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())



l = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# start_time = time.time()
# for i in l :
#     read_info(i)
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"{execution_time} (линейный)") #12.107

if __name__ == '__main__':
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, l)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{execution_time}  (многопроцессный)") #7.158
