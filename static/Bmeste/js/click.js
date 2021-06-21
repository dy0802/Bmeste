const target = document.getElementsByClassName('box');
const target1 = document.getElementsByClassName('box_rect');


for (var i = 0; i < target.length; i++)
{
    eval(target[i].addEventListener('click', function(i){ changeColor("+i+"); }));


}
function changeColor(i)
{
    target1[i].style.fill = "#003876";
}