import {details_location, initializing} from "./map.js";
import {set_streetview} from "./streetview.js";

const target = document.getElementsByClassName('box');
const defaultSet = document.getElementsByClassName('box_rect');

var toggleOnOff = [];

for (var i = 0; i < target.length; i++)
{
    target[i].addEventListener('click', function(){ click_listener(event); });
    toggleOnOff[i] = 0;
}

function click_listener(event)
{
    var k = 0;
    const allContainer = event.currentTarget.parentNode.parentNode.childNodes;
    for (var j = 0; j < allContainer.length; j++)
    {
        if (j%2 == 1)
        {
            if (allContainer[j].childNodes[1].childNodes[1] == event.currentTarget.childNodes[1])
            {
                event.currentTarget.childNodes[1].classList.toggle("active");
                toggleOnOff[k]++;
            }
            else if (toggleOnOff[k]%2 == 1)
            {
                allContainer[j].childNodes[1].childNodes[1].classList.toggle("active");
                toggleOnOff[k]++;
            }
            k++;
        }
    }
    for (var n = 0; n < toggleOnOff.length; n++)
    {
        if (toggleOnOff[n]%2 == 1)
        {
            set_streetview(details_location[n]);
        }
        else
        {
            initializing();
        }
    }
}
