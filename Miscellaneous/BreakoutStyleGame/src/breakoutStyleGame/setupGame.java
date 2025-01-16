package breakoutStyleGame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class setupGame extends JPanel implements KeyListener {
    private static final int WIDTH = 800;  // 화면 너비
    private static final int HEIGHT = 600;  // 화면 높이

    // 공 속성
    private int ballX = WIDTH / 2;
    private int ballY = HEIGHT / 2;
    private int ballRadius = 15;
    private int ballSpeedX = 3;
    private int ballSpeedY = 3;

    // 패들 속성
    private int paddleWidth = 100;
    private int paddleHeight = 15;
    private int paddleX = WIDTH / 2 - paddleWidth / 2;
    private int paddleY = HEIGHT - 50;  // 패들의 y 위치
    private int paddleSpeed = 15;

    // 벽돌 속성
    private final int brickRows = 5;
    private final int brickColumns = 10;
    private final int brickWidth = 60;
    private final int brickHeight = 20;
    private ArrayList<Rectangle> bricks;  // 벽돌 리스트

    public setupGame() {
        this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        this.addKeyListener(this);
        this.setFocusable(true);  // 키보드 입력 활성화

        // 벽돌 초기화
        bricks = new ArrayList<>();
        for (int row = 0; row < brickRows; row++) {
            for (int col = 0; col < brickColumns; col++) {
                int x = col * (brickWidth + 10) + 50;
                int y = row * (brickHeight + 10) + 50;
                bricks.add(new Rectangle(x, y, brickWidth, brickHeight));
            }
        }
    }

    // 패들 그리기
    public void drawPaddle(Graphics g) {
        g.setColor(Color.GREEN);
        g.fillRect(paddleX, paddleY, paddleWidth, paddleHeight);
    }

    // 벽돌 그리기
    public void drawBricks(Graphics g) {
        g.setColor(Color.ORANGE);
        for (Rectangle brick : bricks) {
            g.fillRect(brick.x, brick.y, brick.width, brick.height);
        }
    }

    // 공 움직임 및 충돌 처리
    public void moveBall() {
        ballX += ballSpeedX;
        ballY += ballSpeedY;

        // 벽 충돌
        if (ballX - ballRadius <= 0 || ballX + ballRadius >= WIDTH) {
            ballSpeedX = -ballSpeedX;  // x축 반사
        }
        if (ballY - ballRadius <= 0) {
            ballSpeedY = -ballSpeedY;  // y축 반사
        }

        // 패들 충돌
        if (ballY + ballRadius >= paddleY && ballX >= paddleX && ballX <= paddleX + paddleWidth) {
            ballSpeedY = -ballSpeedY;
            // 공의 속도를 점점 빠르게
            ballSpeedX += (ballSpeedX > 0) ? 1 : -1;
            ballSpeedY += (ballSpeedY > 0) ? 1 : -1;
        }

        // 벽돌 충돌
        for (int i = 0; i < bricks.size(); i++) {
            Rectangle brick = bricks.get(i);
            if (brick.contains(ballX, ballY)) {
                bricks.remove(i);  // 벽돌 제거
                ballSpeedY = -ballSpeedY;  // y축 반사
                break;
            }
        }

        // 바닥에 떨어졌을 때 게임 오버 처리
        if (ballY - ballRadius >= HEIGHT) {
            System.out.println("게임 오버!");
            System.exit(0);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, WIDTH, HEIGHT);

        // 공 그리기
        g.setColor(Color.WHITE);
        g.fillOval(ballX - ballRadius, ballY - ballRadius, ballRadius * 2, ballRadius * 2);

        // 패들 그리기
        drawPaddle(g);

        // 벽돌 그리기
        drawBricks(g);
    }

    // 키보드 입력 처리
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_LEFT && paddleX > 0) {
            paddleX -= paddleSpeed;  // 패들 왼쪽 이동
        }
        if (e.getKeyCode() == KeyEvent.VK_RIGHT && paddleX + paddleWidth < WIDTH) {
            paddleX += paddleSpeed;  // 패들 오른쪽 이동
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void keyTyped(KeyEvent e) {}

    public static void main(String[] args) {
        JFrame frame = new JFrame("Breakout Style Game");
        setupGame gamePanel = new setupGame();
        frame.add(gamePanel);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // 화면 갱신 및 게임 루프
        Timer timer = new Timer(16, e -> {
            gamePanel.moveBall();
            gamePanel.repaint();
        });
        timer.start();
    }
}
