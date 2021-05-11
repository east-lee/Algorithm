inputfiles = open('inputfiles.txt','r')
total_cnt = 0
error_cnt= 0
for inputfile in inputfiles:
    total_cnt += 1
    filename = inputfile.replace('\n','')
    try :
        file = open(filename, 'r+')
        # x = file.read()
        print_result = []
        # 첫번쨰 줄 불러오기
        firstline = file.readline()
        n = int(firstline.replace('base',''))
        for line_idx, line in enumerate(file):
            result = 0
            line = line.replace('\n','')
            line = line[::-1]
            for i in range(len(line)):
                result += int(line[i]) * (n**i)
            line=line[::-1]
            print_result.append(f'{line} {result}')

        result_file = firstline
        for result in print_result:
            result_file += f'{result}\n'
        new_file = open(filename,'w')
        new_file.write(result_file)

    except FileNotFoundError:
        error_cnt += 1
        print(f'The file {filename} is not found')

print(f'{total_cnt - error_cnt} out of {total_cnt} file(s) were processed successfully')