function solution(gift_cards, wants) {
    var answer = 0;
    let not_Using = []
    
    for (let i=0; i<gift_cards.length; i++){
        let new_value = wants[i]
        let break_check = false
        if (not_Using.indexOf(gift_cards[i])>=0) {
            not_Using.splice(not_Using.indexOf(gift_cards[i]),1)
            not_Using.push(new_value)
            continue
        }
        
        for (let j=i;j<wants.length; j++){
            if (gift_cards[i] === wants[j]){
                wants[j] = new_value
                break_check = true
                break
            }
        }
        if (!break_check) {
            answer += 1
            not_Using.push(new_value)
        }
    }      
    return answer;
}