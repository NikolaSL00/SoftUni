public class QueensPuzzle {

    public static char board[][] = {
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'},
            {'-', '-', '-', '-', '-', '-', '-', '-'}
    };

    public static int counter = 0;

    public static void main(String[] args) {
        findQueensPositions(0);
    }

    private static void findQueensPositions(int row) {
        for (int col = 0; col <= 7; col++) {
            if (canPlaceQueen(row, col)) {
                putQueen(row, col);
                if (row == 7) {
                    printSolution();
                    removeQueen(row, col);
                    return;
                }
                findQueensPositions(row + 1);
                removeQueen(row, col);
            }
        }
    }

    private static void putQueen(int row, int col) {
        board[row][col] = '*';
    }

    private static void removeQueen(int row, int col) {
        board[row][col] = '-';
    }

    private static boolean canPlaceQueen(int row, int col) {
        return checkLine("U", row, col)
                && checkLine("D", row, col)
                && checkLine("L", row, col)
                && checkLine("R", row, col)
                && checkLine("UL", row, col)
                && checkLine("UR", row, col)
                && checkLine("DL", row, col)
                && checkLine("DR", row, col);
    }

    // U, D, L, R, UL, UR, DL, DR
    private static boolean checkLine(String direction, int row, int col) {
        if (direction.equals("U")) {
            // row --, col
            for (int i = row; i >= 0; i--) {
                if (board[i][col] != '-') {
                    return false;
                }
            }
        } else if (direction.equals("D")) {
            // row ++, col
            for (int i = row; i <= 7; i++) {
                if (board[i][col] != '-') {
                    return false;
                }
            }
        } else if (direction.equals("R")) {
            // row, col++
            for (int i = col; i <= 7; i++) {
                if (board[row][i] != '-') {
                    return false;
                }
            }
        } else if (direction.equals("L")) {
            // row, col--
            for (int i = col; i >= 0; i--) {
                if (board[row][i] != '-') {
                    return false;
                }
            }
        } else if (direction.equals("UL")) {
            // row--,col--
            int c = col;
            for (int r = row; r >= 0; r--) {
                if (c < 0) {
                    break;
                }
                if (board[r][c] != '-') {
                    return false;
                }
                c--;
            }
        } else if (direction.equals("UR")) {
            // row--, col++
            int c = col;
            for (int r = row; r >= 0; r--) {
                if (c > 7) {
                    break;
                }
                if (board[r][c] != '-') {
                    return false;
                }
                c++;
            }
        } else if (direction.equals("DL")) {
            // row ++, col--
            int c = col;
            for (int r = row; r <= 7; r++) {
                if (c < 0) {
                    break;
                }
                if (board[r][c] != '-') {
                    return false;
                }
                c--;
            }
        } else if (direction.equals("DR")) {
            // row ++, col++
            int c = col;
            for (int r = row; r <= 7; r++) {
                if (c > 7) {
                    break;
                }
                if (board[r][c] != '-') {
                    return false;
                }
                c++;
            }
        }

        return true;
    }


    public static void printSolution() {
        System.out.println("Number of solution: " + ++counter + "\n");
        for (char[] row : board) {
            for (char symbol : row) {
                System.out.print(symbol + " ");
            }
            System.out.println();
        }
        System.out.println("<----------------------------------------------------------->\n");
    }
}
