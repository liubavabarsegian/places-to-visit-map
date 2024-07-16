function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

document.getElementById('rocket').addEventListener('click',function() {
    let c = document.getElementsByClassName('rocket');
    for (let i = 0; i < c.length; i++) {
        c[i].classList.add('animateShake');
        sleep(2000).then(() =>
        c[i].classList.add('animate'));
    }
})