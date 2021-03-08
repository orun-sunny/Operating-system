def Take_Queue():
    input_Queue = (input('Input queue : ')).strip(',');
    array = input_Queue.split(',');
    length_of_queue = len(array);

    return length_of_queue, array;


def Take_head_start():
    head_start = int(input('Input Head Starts : '));
    return head_start


def Take_upper_bound():
    upper_bound = int(input('Upper Bound : '));
    return upper_bound


def Take_lower_bound():
    lower_bound = int(input('Lower Bound : '));
    return lower_bound


def main_process(length_of_queue, head_start, array):
    second_value = head_start;
    Total_distance = 0;
    path = str(head_start);
    head_to_lower_bound = []
    head_to_upper_bound = []
    a=Take_upper_bound()
    b=Take_lower_bound()
    Cal_path=''

    for i in range(0, length_of_queue):
        if int(array[i]) < head_start:
            head_to_lower_bound.append(int(array[i]))
        else:
            head_to_upper_bound.append(int(array[i]))
    empty = []
    for s in range(0, len(head_to_upper_bound) - 1):
        for y in range(0, len(head_to_upper_bound) - 1):
            if head_to_upper_bound[y] > head_to_upper_bound[y + 1]:
                empty = head_to_upper_bound[y]
                head_to_upper_bound[y] = head_to_upper_bound[y + 1]
                head_to_upper_bound[y + 1] = empty
    empty = [];
    for s in range(0, len(head_to_lower_bound) - 1):
        for y in range(0, len(head_to_lower_bound) - 1):
            if head_to_lower_bound[y] < head_to_lower_bound[y + 1]:
                empty = head_to_lower_bound[y]
                head_to_lower_bound[y] = head_to_lower_bound[y + 1]
                head_to_lower_bound[y + 1] = empty

    for z in range(0,len(head_to_lower_bound)):
        if int(head_to_lower_bound[z]) > second_value:
            path = path + ' ' + str(head_to_lower_bound[z])

            Total_distance = Total_distance + (int(head_to_lower_bound[z]) - second_value)
            Cal_path = Cal_path + '('+  str(head_to_lower_bound[z]) + '-' + str(second_value)+')'
            second_value = int(head_to_lower_bound[z])
        else:
            path = path + ' ' + str(head_to_lower_bound[z]);

            Total_distance = Total_distance + (second_value - int(head_to_lower_bound[z]));
            Cal_path = Cal_path  + '('+str(second_value) + '-' + str(head_to_lower_bound[z])+')'
            second_value = int(head_to_lower_bound[z]);

        Cal_path = Cal_path + '+'

    Total_distance = Total_distance + (second_value - b)
    Cal_path = Cal_path  + '(' + str(second_value) + '-' + str(b) + ')'
    Cal_path = Cal_path + '+'
    second_value = b
    path = path + ' ' + str(b)
    for x in range(0, len(head_to_upper_bound)):
        if int(head_to_upper_bound[x]) > second_value:
            path = path + ' ' + str(head_to_upper_bound[x])
            Total_distance = Total_distance + (int(head_to_upper_bound[x]) - second_value)
            Cal_path = Cal_path + '('+ str(head_to_upper_bound[x]) + '-' + str(second_value)+')'
            second_value = int(head_to_upper_bound[x])
        else:
            path = path + ' ' + str(head_to_upper_bound[x])
            Total_distance = Total_distance + (second_value - int(head_to_upper_bound[x]))
            Cal_path = Cal_path  + '('+ str(second_value) + '-' + str(head_to_upper_bound[x])+')'
            second_value = int(head_to_upper_bound[x])
        if x==len(head_to_upper_bound)-1:
            break
        else:
            Cal_path = Cal_path + '+'

    print('Calculation Path : ' + Cal_path)
    print('Total Distance : ' + str(Total_distance))
    print('Path : ' + path)



a, b = Take_Queue()
c = Take_head_start()
main_process(a, c, b)