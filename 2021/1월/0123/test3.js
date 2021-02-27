function solution(next_student) {
    var answer = 0;
    var max_num = 0;
    var n = next_student.length
    var check = new Array(n)
    check.fill(0)
    for (let i=n-1; i>=0;i--){
        if (check[i]!==1){
            var read = new Array(n)
            var now_num = i
            var next_num = next_student[now_num]-1
            var cnt = 1
            read.fill(0)
            
            while (!read[next_num] && next_num!==-1){
                read[now_num] =1 
                check[now_num]=1
                cnt += 1
                now_num = next_num
                next_num = next_student[now_num] -1
            }
            
            if (cnt>max_num) {
                max_num = cnt
                answer = i+1                      
            }   
        }  
    }
    return answer;
}