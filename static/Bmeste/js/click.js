const target = document.getElementsByClassName('box');
const defaultSet = document.getElementsByClassName('box_rect');

for (var i = 0; i < target.length; i++)
{
    target[i].addEventListener('click', function(){ click_listener(event); });
}

function click_listener(event)
{
    console.log("clicked!");
    allContainer=event.currentTarget.parentNode.parentNode.childNodes;

    for (var j = 0; j < allContainer.length; j ++)
    {
        var k = 0;
        if (j%2 == 1)
        {
            if (allContainer[j].childNodes[1] != event.target)
            {
                allContainer[j].childNodes[1].childNodes[1].style = defaultSet[k].style;
            }
            k += 1;
        }
    }
    event.currentTarget.childNodes[1].style.fill="#003876";
}