def input_data():
    input_total_process = int(input('How many process take input : '));
    array = [];
    for x in range(0, input_total_process):
        a = 'p' + str(x + 1);
        burst_time = int(input('burst time for ' + a + ': '));
        Priority = int(input('Priority for ' + a + ': '));
        b = [a, burst_time, Priority];
        array.append(b);

    empty = [];
    for s in range(0, len(array) - 1):
        for y in range(0, len(array) - 1):
            if array[y][2] > array[y + 1][2]:  # compare here
                empty = array[y]
                array[y] = array[y + 1]  # saved
                array[y + 1] = empty

    return array, input_total_process


def main_function(array, input_total_process):
    time = 0
    total_time = 0
    chart = ''

    string = ''
    for z in range(0, len(array)):
        time = time + array[z][1]
        chart = chart + array[z][0]
        if (z < len(array) - 1):
            total_time = total_time + time
        string = string + ' ' + array[z][0] + ' ' + str(time)
    print('GANTT Chart : ' + '0' + string)
    average_wating_time = total_time / input_total_process
    print('Average time will be : ' + str(average_wating_time))


a, b = input_data()

main_function(a, b)
