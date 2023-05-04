console.log("hello")


const button = document.getElementsByClassName('btn')
const count = document.getElementById('count')

for(i=0; i<button.length; i++){
    button[i].addEventListener('click', (e) =>{
        if (e.target.classList.contains('inc-btn')){
            count.innerHTML++
        }else if (e.target.classList.contains('dec-btn')){
            count.innerHTML--
        } if (e.target.classList.contains('rst-btn')){
            count.innerHTML=0
        }
    })
}