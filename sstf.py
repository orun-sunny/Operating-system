def Take_Queue():
    input_Queue = (input('Input queue : ')).strip(','); #take input
    array = input_Queue.split(','); #take index
    length_of_queue = len(array);

    return length_of_queue, array;


def Take_head_start():
    head_start = int(input('Input Head Starts : '));
    return head_start


def main_function():
    length_of_queue, array = Take_Queue() #func call
    head_start = Take_head_start()
    sum = 0
    path=str(head_start)
    TwoDArray = []
    for i in range(0, len(array)):
        value_head_difference = [int(array[i]), head_start,0]
        TwoDArray.append(value_head_difference)
    for z in range(length_of_queue,0,-1):
        value_head_difference = []
        finding_min = []
        for m in range(0, len(TwoDArray)):
            TwoDArray[m][2]=(abs(TwoDArray[m][0]-TwoDArray[m][1]))
            finding_min.append(TwoDArray[m][2])
       # print(TwoDArray)
        minimum = min(finding_min)
        #print(minimum)
        for j in range(0, len(TwoDArray)):
            if TwoDArray[j][2] == minimum:

                sum = sum + TwoDArray[j][2]
                print(sum)
                for k in range(0, len(TwoDArray)):
                    TwoDArray[k][1] = TwoDArray[j][0]
                head_start = TwoDArray[j][1]
                a=TwoDArray[j]
        path = path + ' ' + str(a[1])
        TwoDArray.remove(a)

        length_of_queue=int(len(TwoDArray))
       # print(len(TwoDArray))
       # print(TwoDArray)
        print('Total distance :'+str(sum))
        print('Path : '+path)


main_function()