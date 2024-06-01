import pygame



def game_over_window(score, window, window_width, window_height):

    font = pygame.font.Font(None,48)
    if score == 2590:
        text = font.render("You Win!", True, (255,255,255))
    else:
        text = font.render("Game Over", True, (255,255,255))  
    text_rect = text.get_rect(center=(window_width//2, window_height//2 - 50))
    window.blit(text,text_rect)
    
    restart_button = pygame.Rect(window_width//2 - 100, window_height//2, 200, 50)
    restart_text = font.render("Restart",True,(0,0,0))
    restart_text_rect = restart_text.get_rect(center=restart_button.center)

    close_button = pygame.Rect(window_width//2 -100, window_height//2 + 70, 200, 50)
    close_text = font.render("Close",True,(0,0,0))
    close_text_rect = close_text.get_rect(center=close_button.center)
    

    background_margin = 20  # Space around the elements
    background_x = min(text_rect.left, restart_button.left, close_button.left) - background_margin
    background_y = min(text_rect.top, restart_button.top, close_button.top) - background_margin
    background_width = max(text_rect.right, restart_button.right, close_button.right) - background_x + 2 * background_margin
    background_height = max(text_rect.bottom, restart_button.bottom, close_button.bottom) - background_y + 2 * background_margin

    background_rect = pygame.Rect(background_x, background_y, background_width, background_height)
    pygame.draw.rect(window, (0, 0, 0), background_rect)  # Black rectangle

    # Draw everything else on top
    window.blit(text, text_rect)
    pygame.draw.rect(window, (50, 205, 50), restart_button)  
    pygame.draw.rect(window, (255, 0, 0), close_button)  

    window.blit(restart_text, restart_text_rect) 
    window.blit(close_text, close_text_rect) 
    
    return restart_button, close_button

def check_pacman_lost(pacman,ghosts):
    pacman_row,pacman_col = pacman.row, pacman.col
    for ghost in ghosts:
        if ghost.y == pacman_row and ghost.x == pacman_col:
            return True
    return False    

