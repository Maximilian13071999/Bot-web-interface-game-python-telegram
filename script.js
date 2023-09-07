let tg = window.Telegram.WebApp
tg.expand()

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FF8979"

let player = document.querySelector("#player")
let bomb = document.querySelector("#bomb")
let scores = document.querySelector("#scores")
let score = 0
let result = ""

function win_check() {
    if (score >= 3) {
        player.style.display = "none"
        bomb.style.display = "none"
        document.querySelector("body").style.background = "url(https://www.block-chain24.com/sites/default/files/styles/full_bg/public/img/maxresdefault_19.jpg?itok=fxGktJqY)"
        clearInterval(timer)
        tg.MainButton.setText("Вы выиграли!")
        result = "win"
        tg.MainButton.show()
    }
}

function lose_check() {
    if (score <= -3) {
        player.style.display = "none"
        bomb.style.display = "none"
        document.querySelector("body").style.background = "url(https://t3.ftcdn.net/jpg/00/76/48/34/360_F_76483432_NWp7msjfeC7bsIpcMq03QRH1CuIeWQYj.jpg)"
        clearInterval(timer)
        tg.MainButton.setText("Вы проиграли!")
        result = "lose"
        tg.MainButton.show()
    }
}

player.onclick = () => {
    score += 1
    scores.innerHTML = "Score: " + score
}

bomb.onclick = () => {
    score -= 1
    scores.innerHTML = "Score: " + score
}

Telegram.WebApp.onEvent("mainButtonClicked", function() {
    tg.sendData(result)
})

let timer = setInterval(function() {
    let chance = Math.random()
    if (chance > 0.5) {
        player.style.display = "none"
        bomb.style.display = "block"
        win_check()
    } else {
        player.style.display = "block"
        bomb.style.display = "none"
        lose_check()
    }
    player.style.top = Math.random() * 500 + "px"
    player.style.left = Math.random() * 290 + "px"
    bomb.style.top = Math.random() * 500 + "px"
    bomb.style.left = Math.random() * 290 + "px"
}, 800)