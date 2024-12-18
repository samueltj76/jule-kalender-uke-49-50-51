import pygame
import sys
from datetime import datetime

# Initialiser pygame
pygame.init()

# størelse på pygamet og farger
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("jule kalender")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Velger skrifttype
font = pygame.font.Font(None, 36)

# bruker grid til å ette opp alle de 24 lukene (6*4)
GRID_ROWS, GRID_COLS = 6, 4
CELL_WIDTH = WIDTH // GRID_COLS
CELL_HEIGHT = HEIGHT // GRID_ROWS
DOOR_COUNT = GRID_ROWS * GRID_COLS

# Liste for å holde styr på dører som er åpne
opened_doors = [False] * DOOR_COUNT

# Henter dagens dato 
today = datetime.now().day

#Denne funksjonen  viser hvordan julekalenderen ser ut og hva som skjer når en dør åpnes#
def draw_grid():
    
    for row in range(GRID_ROWS):#gjør at grid rown og grid cols blir tegnet
        for col in range(GRID_COLS):#gjør at grid rown og grid cols blir tegnet

            #Koden beregner posisjonen til hver celle i gridet
            index = row * GRID_COLS + col
            x = col * CELL_WIDTH #Beregner den horisontale posisjonen for cellen i piksler
            y = row * CELL_HEIGHT #Beregner den vertikale posisjonen for cellen i piksler
             # Tegner åpnet eller lukket dør. 
            if opened_doors[index]:
                pygame.draw.rect(screen, WHITE, (x, y, CELL_WIDTH, CELL_HEIGHT)) #hvis døren er open skal fargen på luken være hvit.
                text = font.render(f"Day {index + 1}", True, BLACK) #hvis døren er open lager text for datoen som for eksempel day 1.
                screen.blit(text, (x + 20, y + 20))
            else:
                pygame.draw.rect(screen, RED, (x, y, CELL_WIDTH, CELL_HEIGHT)) #hvis døren ikke er open skal fargen på døren være rød.
            # Tegner kantlinje
            pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT), 2)

#Håndter åpning av dører basert på museklikk
def open_door(pos):
    x, y = pos
    #beregner hvilke dør som blir klikket
    col = x // CELL_WIDTH
    row = y // CELL_HEIGHT
    index = row * GRID_COLS + col
    # Sjekker om døren kan åpnes
    if index < DOOR_COUNT and not opened_doors[index]:
      if index + 1 <= today:#gjør at det Kun åpne dører opp til dagens dato
            opened_doors[index] = True

#Hovedløkken for kalenderen
def main():
    
    clock = pygame.time.Clock() #klokke i pygame som kontrolere datoen

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:# lukker programmet hvis du lukker vindue
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #åpner en dør med et museklikk
                open_door(event.pos)

        # Tegn gridet og oppdater skjermen
        draw_grid()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

