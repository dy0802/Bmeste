import {toggleOnOff} from "./click.js";

const toggleBtn = document.querySelector('.box_discript');
const trigger = document.querySelector('.trigger');
const mask = document.querySelector('.mask');
const modalWrapper = document.querySelector('.modal-wrapper');
const piece_detail = document.querySelectorAll('#piece_detail');
const description = document.querySelectorAll('#description');
const detail_title = document.getElementsByClassName("detail_title")[0];
const detail_description = document.getElementsByClassName("detail_description")[0];

toggleBtn.addEventListener('click', () => {
    modalWrapper.classList.toggle('open');
    toggleBtn.classList.toggle('active');
    mask.classList.toggle('active');

    let sum = 0;
    for (let k = 0; k < toggleOnOff.length; k++)
    {
        sum += toggleOnOff[k];
    }
    if (sum%2 == 0)
    {
        detail_title.innerText = "장소를 선택해주세요!";
        detail_description.innerText = "이곳에 작품에 대한 설명이 나옵니다:)";
    }
    else
    {
        for (var n = 0; n < toggleOnOff.length; n++)
        {
            if (toggleOnOff[n]%2 == 1)
            {
                let i = 0;
                i = n + 1;
                detail_title.innerText = i + ". " + JSON.parse(piece_detail[n].textContent);
                detail_description.innerText = JSON.parse(description[n].textContent);
            }
        }
    }
});

trigger.addEventListener('click', () => {
    modalWrapper.classList.toggle('open');
    toggleBtn.classList.toggle('active');
    mask.classList.toggle('active');
});