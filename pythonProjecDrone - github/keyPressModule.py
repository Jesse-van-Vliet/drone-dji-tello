import pygame


def init():
    pygame.init()
    # Control window size here (width, height) as 400x400 pixels
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    # Return True if key is pressed down and False otherwise
    ans = False
    # Check if the key is pressed down
    for eve in pygame.event.get(): pass
    # Get the list of all the keys that are pressed down
    keyInput = pygame.key.get_pressed()
    # Get the value of the key that we are interested in
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    # Check if the key is pressed down
    if keyInput[myKey]:
        # If yes, then return True and exit the loop otherwise return False and exit the loop
        ans = True
    # Update the display
    pygame.display.update()
    # Return the value
    return ans


def main():
    # Print the value of the key that is pressed down
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()
