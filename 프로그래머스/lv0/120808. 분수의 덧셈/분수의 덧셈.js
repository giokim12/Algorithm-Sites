function solution(denum1, num1, denum2, num2) {
    const ansTop = denum1 * num2 + denum2 * num1
    const ansBottom = num1 * num2
    
    let minNumber
    if (ansTop<ansBottom) {
        minNumber = ansTop
    } else {
        minNumber = ansBottom
    }
    
while(true) {   
    if (ansTop % minNumber === 0) {
        if (ansBottom % minNumber === 0) {
           return [ansTop/minNumber, ansBottom/minNumber] 
        }
    }
    minNumber = minNumber -1
    }
}