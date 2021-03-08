def Take_Queue():
    input_Queue = input('Input queue : ');
    array = input_Queue.split(',');
    length_of_queue = len(array);
    return length_of_queue,array;

def Take_head_start():
    head_start = int(input('Input Head Starts : '));
    return head_start
def main_process(length_of_queue,head_start,array):
    second_value=head_start;
    Total_distance=0;
    path=str(head_start);

    for x in range(0,length_of_queue):
        if int(array[x]) > second_value:
            path=path+' '+array[x];
            Total_distance=Total_distance+(int(array[x])-second_value);
            second_value=int(array[x]);
        else:
            path = path + ' ' + array[x];
            Total_distance=Total_distance+(second_value-int(array[x]));
            second_value=int(array[x]);
    print('Total Distance : '+ str(Total_distance));
    print('Path : '+path);

a,b=Take_Queue();
c=Take_head_start();
main_process(a,c,b)