package tictactoe;

import java.util.ArrayList;
import java.util.List;

public class MainGame {

    private char[] board;
    private char currentPlayer;

    public MainGame() {
        board = new char[9];
        currentPlayer = 'X';
        initializeBoard();
    }

    //Gives us access to currentPlayerMark
    public char getCurrentPlayer()
    {
        return currentPlayer;
    }
    
    //Gives us access to currentPlayerMark
    public char getOtherPlayer()
    {
        char player;
        if(currentPlayer == 'X')  player = 'O';
        else player = 'X';
        return player;
    }
    
    public char[] getCurrentBoard()
    {
        return board;
    }

    // Set/Reset the board back to all empty values.
    public void initializeBoard() {

        // Loop through array
        for (int i = 0; i < 9; i++){
                board[i] = '-';
            }
    }
    public void makeBoard(char[] newBoard) {

        // Loop through array
        for (int i = 0; i < 9; i++){
                board[i] = newBoard[i];
            }
    }


    // Print the current board (may be replaced by GUI implementation later)
    public void printBoard() {
        System.out.println("-------------");
        int count = 0;
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[count] + " | ");
                count++;
            }
            System.out.println();
            System.out.println("-------------");
        }
    }


    // Loop through all cells of the board and if one is found to be empty (contains char '-') then return false.
    // Otherwise the board is full.
    public boolean isBoardFull() {
        boolean isFull = true;

        for (int i = 0; i < 9; i++) {
                if (board[i] == '-') {
                    isFull = false;
                }
        }
        return isFull;
    }


    // Returns true if there is a win, false otherwise.
    // This calls our other win check functions to check the entire board.
    public boolean isWinner(char player) {
       /* char player;
        if(play == 'X') player = 'O';
        else player = 'X';*/
        boolean isWin = false;
        if(
                (board[0] == player && board[1] == board[0] && board[2] == board[0]) ||
                (board[3] == player && board[4] == board[3] && board[5] == board[3]) ||
                (board[6] == player && board[7] == board[6] && board[8] == board[6]) ||
                (board[0] == player && board[3] == board[0] && board[6] == board[0]) ||
                (board[1] == player && board[4] == board[1] && board[7] == board[1]) ||
                (board[2] == player && board[5] == board[2] && board[8] == board[2]) ||
                (board[0] == player && board[4] == board[0] && board[8] == board[0]) ||
                (board[2] == player && board[4] == board[2] && board[6] == board[2])
                ) isWin = true;
        return isWin;
    }
    

    // Change player marks back and forth.
    public void changePlayer() {
        if (currentPlayer == 'X') {
            currentPlayer = 'O';
        }
        else {
            currentPlayer = 'X';
        }
    }

    // Places a mark at the cell specified by row and col with the mark of the current player.
    public boolean placeMark(int mark) {

        // Make sure that row and column are in bounds of the board.
        if ((mark >= 0) && (mark < 9)) {
                if (board[mark] == '-') {
                    board[mark] = currentPlayer;
                    return true;
                }
        }
        return false;
    }
    public void removeMark(int mark) {

        board[mark] = '-';
    }
    
    public boolean isMark(int mark){
        return board[mark] != '-';
    }
    
    public ArrayList availableSpots(){
        ArrayList<Integer> avail = new ArrayList<>();
        for(int i = 0; i < 9; i++){
            if(board[i] == '-'){
                avail.add(i);
            }
        }
        //System.out.println(avail.size());
        return avail;
    }

}


