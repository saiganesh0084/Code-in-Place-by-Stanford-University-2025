from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range(BRICKS_IN_BASE):
        # Calculate number of bricks in current row
        bricks_in_row = BRICKS_IN_BASE - row
        
        # Calculate the y-coordinate for this row (bottom up)
        # Start from bottom of canvas and work upward
        bottom_y = CANVAS_HEIGHT - (row * BRICK_HEIGHT)
        top_y = bottom_y - BRICK_HEIGHT
        
        # Calculate total width of this row
        row_width = bricks_in_row * BRICK_WIDTH
        
        # Calculate starting x-coordinate to center the row
        start_x = (CANVAS_WIDTH - row_width) // 2
        
        # Draw each brick in this row
        for brick in range(bricks_in_row):
            # Calculate x-coordinates for this brick
            left_x = start_x + (brick * BRICK_WIDTH)
            right_x = left_x + BRICK_WIDTH
            
            # Draw the brick
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                "orange",  # Fill color
                "black"    # Outline color
            )

if __name__ == '__main__':
    main()