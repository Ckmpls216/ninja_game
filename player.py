import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.index = 0
        self.load_images()  # Load and scale images
        self.image = self.idle_images[self.index]  # Set the initial image
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

        # Movement attributes
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.5

    def load_images(self):
        # Load the idle animation images and scale them down
        self.idle_images = []
        for i in range(1, 11):
            img_path = os.path.join('img', 'player', 'idle', f'idle_{i}.png')
            image = pygame.image.load(img_path).convert_alpha()

            # Get the dimensions and scale down
            width = image.get_width() // 4
            height = image.get_height() // 4
            
            # Scale the image to new dimensions
            image = pygame.transform.scale(image, (width, height))
            self.idle_images.append(image)

        # Load and scale running animation images
        self.running_images_right = []
        self.running_images_left = []
        for i in range(1, 11):
            img_path = os.path.join('img', 'player', 'run', f'run_{i}.png')
            image = pygame.image.load(img_path).convert_alpha()
            width = image.get_width() // 4
            height = image.get_height() // 4
            image_scaled = pygame.transform.scale(image, (width, height))
            self.running_images_right.append(image_scaled)
            image_flipped = pygame.transform.flip(image_scaled, True, False)
            self.running_images_left.append(image_flipped)

    def update(self):
        # Handle left and right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move_left()
        elif keys[pygame.K_d]:
            self.move_right()
        else:
            self.stop()

        # Update the animation
        self.animate()

        # Apply gravity
        self.velocity.y += self.gravity
        self.rect.y += int(self.velocity.y)

        # Apply Horizontal Movement
        self.rect.x += int(self.velocity.x)

    def animate(self):
        # Determine if we should use the idle or running animation
        if self.velocity.x > 0:
            self.index += 0.1
            if self.index >= len(self.running_images_right):
                self.index = 0
            self.image = self.running_images_right[int(self.index)]
        elif self.velocity.x < 0:
            self.index += 0.1
            if self.index >= len(self.running_images_left):
                self.index = 0
            self.image = self.running_images_left[int(self.index)]
        else:
            # If not moving, animate idle
            self.index += 0.1
            if self.index >= len(self.idle_images):
                self.index = 0
            self.image = self.idle_images[int(self.index)]

    def move_left(self):
        self.velocity.x = -self.speed

    def move_right(self):
        self.velocity.x = self.speed

    def stop(self):
        self.velocity.x = 0

    def draw(self, surface):
        # Draw the Sprite at the center of the screen
        center_x = surface.get_width() // 2
        center_y = surface.get_height() // 2
        surface.blit(self.image, (center_x - self.rect.width // 2, center_y - self.rect.height //2))
