function ale(n){
    if (n % 2 == 0) {
        return "odd"
    }
    else{
        return "even"
    }
}

const func = ale;
console.log(func(34))