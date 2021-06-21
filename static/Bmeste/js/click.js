const target = document.getElementsByClassName('box');

for (const i = 0; i < target.length; i++)
{
    target[i].addEventListener('click', function(){ changeColor(i); });
}
function changeColor(a)
{
    console.log(a);
    document.getElementsByClassName('box_rect')[a].style.fill = "#003876";
}