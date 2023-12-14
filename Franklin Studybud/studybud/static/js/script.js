window.addEventListener('DOMContentLoaded', function(e){
    let collections = document.querySelector('.slide-border');
    let images = document.querySelectorAll('.image-slides');

    // console.log(collections, images);

    // for (let i = 1; i < images.length; i++) {
    //     let cal = 1;
    //     setTimeout(function(){
    //         let calculation = -29 * 2
    //         collections.style.transform = `translateX(${calculation}rem)`
    //         cal++
    //     }, 2000)
    // }

    let i = 1;
    while (i < images.length) {
        // let cal = 1;
        setTimeout(function(){
            let calculation = -29 * i
            collections.style.transform = `translateX(${calculation}rem)`
            // cal++
        }, 2000)
    }
})