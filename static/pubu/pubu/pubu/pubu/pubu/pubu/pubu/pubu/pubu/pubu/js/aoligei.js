$(document).ready(function () {
    document.documentElement.style.fontSize=innerWidth/10+"px";
    setTimeout(function () {
       swiper1()
       initSwiperMenu()
    },100)

})

function swiper1() {
    var mySwiper = new Swiper ('#topSwiper', {

        // 轮播图的方向，也可以是vertical方向

        direction:'horizontal',

        //播放速度

        loop: true,

        // 自动播放时间

        autoplay:true,


        speed:2000,


      pagination: {
            el: '.swiper-pagination',
            clickable:true,

      },
　　// 这样，即使我们滑动之后， 定时器也不会被清除

　　autoplayDisableOnInteraction : false,

      })
    for(i=0;i<mySwiper.pagination.bullets.length;i++){
  mySwiper.pagination.bullets[i].onmouseover=function(){
    this.click();
  };
  }
  //如果你在swiper初始化后才决定使用clickable，可以这样设置
mySwiper.params.pagination.clickable = true ;
//此外还需要重新初始化pagination
mySwiper.pagination.destroy()
mySwiper.pagination.init()
mySwiper.pagination.bullets.eq(0).addClass('swiper-pagination-bullet-active');
}
function initSwiperMenu() {
    var swiper = new Swiper("#swiperMenu",{
       slidesPerView: 2,
        spaceBetween:2,
    });
}