document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll(".cell");
    const message = document.getElementById("message");
    const newGameButton = document.getElementById("new-game");

    let currentPlayer = "X";
    let gameBoard = ["", "", "", "", "", "", "", "", ""];
    let gameActive = true;

    const winningCombos = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    const checkWinner = () => {
        for (const combo of winningCombos) {
            const [a, b, c] = combo;
            if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
                gameActive = false;
                cells[a].classList.add("winner");
                cells[b].classList.add("winner");
                cells[c].classList.add("winner");
                message.innerText = `Player ${gameBoard[a]} wins!`;
            }
        }

        if (!gameBoard.includes("") && gameActive) {
            gameActive = false;
            message.innerText = "It's a draw!";
        }
    };

    cells.forEach((cell, index) => {
        cell.addEventListener("click", () => {
            if (!gameActive || gameBoard[index] !== "") return;
            gameBoard[index] = currentPlayer;
            cell.innerText = currentPlayer;
            cell.classList.add(currentPlayer);
            currentPlayer = currentPlayer === "X" ? "O" : "X";
            message.innerText = `Player ${currentPlayer}'s turn`;
            checkWinner();
        });
    });

    newGameButton.addEventListener("click", () => {
        cells.forEach((cell) => {
            cell.innerText = "";
            cell.classList.remove("X", "O", "winner");
        });
        gameBoard = ["", "", "", "", "", "", "", "", ""];
        currentPlayer = "X";
        gameActive = true;
        message.innerText = "Player X's turn";
    });
});
