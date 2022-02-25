# pyasteroids

An Asteroids clone, made with python and pyglet. Docs: https://pyglet.readthedocs.io/en/latest/index.html
Art from opengameart.org.


# TODO:
- Draw player and a few asteroids
- Asteroids come in 3 sizes: big, medium, small.
- Asteroids move in random directions at constant speeds
- Player moves as follows:
  - W -> Moves the player in the direction the player is facing
  - A -> Rotate the player counter-clockwise
  - D -> Rotate the player clockwise
  - S -> Brake, that is, gradually reduces speed
  - Player is in space, so speed remains constant if no outside force
- The player and asteroids loop to the other side when going over the border of the screen
- Player can shoot bullets
  - Bullets move in a constant speed, in the direction the player was facing when fired
  - Apply a cooldown for shooting bullets. That is, at most one bullet every, say, 0.3 seconds.
  - Bullets that go outside the screen are destroyed.
- Collision checking with asteroids(See: AABB collision)
  - If player collides with an asteroid, remove one life. If last life, game over. Player starts with 3
  - If a bullet collides with an asteroid, destroy the bullet and the asteroid.
- Asteroids split when destroyed:
  - If it's a big asteroid, it splits into 3 medium ones.
  - If it's a medium asteroid, it splits into 3 small ones.
  - If it's a small asteroid, it doesn't split.
- Split asteroids gain a random increase in speed as well as a reasonable change in direction
- Asteroid spawning:
  - Spawn a group of asteroids as soon as there are no more
  - Asteroids spawn around the edges of the screen
  - Asteroids never spawn on top of the player
- Sound(See (Bfxr)[https://www.bfxr.net]):
  - Shooting bullets plays a shooty sound
  - Asteroids being destroyed plays an appropriate sound
  - Moving with W activates the engine, playing an engine humming sound
- HUD
  - Draw current score.
  - Show a heart(or similar) for each life left.
- Scoring:
  - Destroying asteroids increases score.
  - Dying resets the score.

Additional polish:
- Game over screen:
  - Show score
  - Button to restart the game
- Pause screen: ESC to pause
  - Nothing moves, nothing is processed
  - Draw the words "PAUSED" while paused
  - ESC again to unpause