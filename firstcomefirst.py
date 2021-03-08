def input_data():
    input_total_process = int(input('Take Input : '));  # take input
    burst_time_array = [];
    process_array = [];
    for x in range(1, input_total_process + 1):
        a = 'p' + str(x);
        process_array.append(a);
        burst_time = input('Process ' + a + ': ');  # take burst time

        burst_time_array.append(int(burst_time));
    return burst_time_array, input_total_process, process_array;


def average_time(burst_time_array, input_total_process):
    time = 0;
    total_time = 0;

    waitng_time_Array = [];
    for y in range(0, len(burst_time_array)):
        time = time + int(burst_time_array[y]);
        waitng_time_Array.append(time);
        if (y < len(burst_time_array) - 1):
            total_time = total_time + time;

    average_time = int(total_time) / int(input_total_process);
    print('Average time will be : ' + str(average_time));
    return waitng_time_Array;


def gantt_chart(waitng_time_Array, process_array):
    chart = '';
    for z in range(0, len(waitng_time_Array)):
        element = process_array[z] + ' ' + str(waitng_time_Array[z]);
        chart = chart + ' ' + element;

    print('GANTT Chart : ' + '0' + chart);


a, b, c = input_data();
d = average_time(a, b);
gantt_chart(d, c);
