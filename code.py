
import sys
import math


def find_median(input_list):
    input_list.sort()
    n = len(input_list)
    if n % 2 == 0:
        median1 = input_list[n // 2]
        median2 = input_list[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = input_list[n // 2]
    return median


def find_variance(input_list, avg, count):
    var = 0
    for val in input_list:
        var = var + ((val - avg) ** 2)
    return var / (count - 1)


def find_standard_deviation(val):
    return math.sqrt(val)


def find_average(input_list):
    return sum(input_list)/len(input_list)


def main():

    count = 0
    valid_num_count = 0
    numbers = []

    file_name = sys.argv[1]
    column_to_parse = int(sys.argv[2])
    with open(file_name, 'r') as infile:
        for line in infile:
            try:
                col_val = float(line.split()[column_to_parse])
                if math.isnan(col_val):
                    count = count+1
                else:
                    count = count+1
                    valid_num_count = valid_num_count+1
                    numbers.append(col_val)
            except IndexError:
                print("There is no valid 'list index' in column %s in line %s in file :%s" % (str(column_to_parse), str(count + 1), file_name))

                exit()
            except ValueError:
                count = count+1
                print("Skipping line number %s : could not convert string to float : %s" % (str(count), str(line.split()[column_to_parse])))

    if valid_num_count == 0:
        print("There were no valid number(s) in column %s in file: %s" % (str(column_to_parse), file_name))

    else:
        average = find_average(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
        variance = find_variance(numbers, average, count)
        standard_deviation = find_standard_deviation(variance)
        median = find_median(numbers)
        print("\tColumn: %d" % column_to_parse)
        print("\n")
        print(count, valid_num_count, average, maximum, minimum, variance, standard_deviation, median)


if __name__ == '__main__':
    main()
