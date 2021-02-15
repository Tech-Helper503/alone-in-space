from ursina import *                    
from ursina.prefabs.first_person_controller import FirstPersonController


window.title = 'My Game'               
window.borderless = False               
window.fullscreen = False               
window.exit_button.visible = False 
window.fps_counter.enabled = True


app = Ursina()                           
player = FirstPersonController()

def update():
	if held_keys['w'] or held_keys['up arrow']:
		player.position = Vec3(
			player.position.x,
			player.position.y,
			player.position.z += vel * dt
		)


	if held_keys['a'] or held_keys['left arrow']:
		player.position = Vec3(
			player.position.x -= vel * dt,
			player.position.y,
			player.position.z 
		)

	if held_keys['s'] or held_keys['down arrow']:
		player.position = Vec3(
			player.position.x,
			player.position.y,
			player.position.z -= vel * dt
		)
	if held_keys['d'] or held_keys['right arrow']:
		player.position = Vec3(
			player.position.x += vel * dt,
			player.position.y,
			player.position.z
		)

app.run()