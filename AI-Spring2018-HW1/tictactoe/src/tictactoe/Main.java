package tictactoe;
import static java.lang.Integer.max;
import static java.lang.Integer.min;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
     
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        MainGame game = new MainGame();
       // nonPlayer opp = new nonPlayer();
        game.initializeBoard();
        
        System.out.println("Tic-Tac-Toe!");
        do
        {
            System.out.println("Current board layout:");
            game.printBoard();
            int mark;
            do
            {
                if(game.getCurrentPlayer() == 'X'){
                    System.out.println("Player " + game.getCurrentPlayer() + ", enter an empty location 1-9!");
                    mark = scan.nextInt()-1;
                }
                else{
                    mark = minimax(game.getCurrentBoard(), 0);
                }
                
            }
            
            while (!game.placeMark(mark));{      
            game.changePlayer();
            //System.out.println(minimax(game));
        }
        }
        while(!game.isWinner(game.getOtherPlayer()) && !game.isBoardFull());
        if (game.isBoardFull() && !game.isWinner(game.getOtherPlayer()))
        {
            game.printBoard();
            System.out.println("CATS GAME!");
        }
        else
        {
            System.out.println("Current board layout:");
            game.printBoard();
            game.changePlayer();
            System.out.println(game.getCurrentPlayer() + " IS THE WINNER!");
        }
    }

      private static int minimax(char[] board, int depth){
            int bestMove = 0;
            int score = Integer.MAX_VALUE;
            for (int i = 0; i < 9; i++){
                if(board[i] != '-') continue;
                board[i] = 'O';
                int temp = maxxer(board, 0, depth);
                if(temp < score){
                    score = temp;
                    bestMove = i;
                }
                board[i] = '-';      
            }
            return bestMove;
      }
      
    private static int maxxer(char[] board, int level, int depth) {
        MainGame tempGame = new MainGame();
        tempGame.makeBoard(board);
        tempGame.printBoard();
        if(tempGame.isWinner('X')) return 10;
        else if(tempGame.isWinner('O')) return -10;
        else if(tempGame.isBoardFull() || depth <= 0) return 0;
        int min = Integer.MIN_VALUE;
        depth = depth-1;
        for (int i = 0; i < 9; i++){
            if(board[i] == '-'){
                board[i] = 'X';
                min = max(min, minner(board, level+1, depth)-level);
                board[i] = '-';
            }
        }
        return min;
    }

    private static int minner(char[] board, int level, int depth) {
        MainGame tempGame = new MainGame();
        tempGame.makeBoard(board);
        tempGame.printBoard();
        if(tempGame.isWinner('X')) return 10;
        else if(tempGame.isWinner('O')) return -10;
        else if(tempGame.isBoardFull() || depth <= 0) return 0;
        int max = Integer.MAX_VALUE;
        depth = depth-1;
        for (int i = 0; i < 9; i++){
            if(board[i] == '-'){
                board[i] = 'O';
                max = min(max, maxxer(board, level+1, depth)+level);
                board[i] = '-';
            }
        }
        
        return max;
    }
            
}
