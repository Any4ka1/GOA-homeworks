const btn3 = document.getElementById('btn3');

const hoe4 = document.getElementById('hoe4');
const btn4 = document.getElementById('btn4');

btn1.addEventListener('click', function(){
    hoe1.textContent = 'i dont remember'
})

btn2.addEventListener('dblclick', function(){
    hoe2.textContent = 'la baguette'
})

btn3.addEventListener('mouseover', function(){
    hoe3.textContent = 'dkdk'
})

btn4.addEventListener('mouseout', function(){
    hoe4.textContent = ''
})

btn1.style.backgroundColor = 'purple'

btn1.style.width = "250px";
btn1.style.height = "100px";