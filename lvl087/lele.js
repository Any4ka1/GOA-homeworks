function listMap(list, func) {
  let result = [];
  for (let i = 0; i < list.length; i++) {
    result.push(func(list[i]));
  }
  return result;
}

function evenOrOdd(num) {
  return num % 2 === 0 ? "even" : "odd";
}