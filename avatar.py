from settings import *
from layer import Layer


class AvatarGenerator:
	def __init__(self, images_path):
		self.layers = self.load_image_layers(images_path)
		self.output_path = OUT_PATH
		os.makedirs(self.output_path, exist_ok=True)


	def load_image_layers(self, images_path):
		sub_paths = sorted(os.listdir(images_path))
		layers = []
		for sub_path in sub_paths:
			layer_path = os.path.join(images_path, sub_path)
			layer = Layer(layer_path)
			layers.append(layer)
		for i, rarity in enumerate(LAYER_RARITIES):
			layers[i].rarity = rarity
		return layers


	def generate_image_sequence(self, i):
		image_path_sequence = []
		for layer in self.layers:
			if layer.should_generate():
				image_path = layer.get_random_image_path(image_path_sequence)
				image_path_sequence.append(image_path)
				if 'special' in image_path:
					print('special: ' + str(i))
		return image_path_sequence


	def render_avatar_image(self, image_path_sequence, i):
		bg_extracted = random.random() * 100
		if bg_extracted > 99.9:
			print('supreme: ' + str(i))
		for rarity, bg in BGS.items():
			rarity_range = list(map(float, rarity.split('-')))
			if rarity_range[0] <= bg_extracted <= rarity_range[1]:
				bg_color = bg
				break
		else:
			bg_color = (0, 0, 0)
		image = Image.new("RGBA", IMG_SIZE, bg_color)
		for image_path in image_path_sequence:
			layer_image = Image.open(image_path)
			image = Image.alpha_composite(image, layer_image)
		return image


	def save_image(self, image, i):
		image_index = str(i).zfill(4)
		image_file_name = f"{image_index}.png"
		image_save_path = os.path.join(self.output_path, image_file_name)
		image.save(image_save_path)


	def generate_avatar(self, n = 1):
		for i in range(n):
			image_path_sequence = self.generate_image_sequence(i)
			#image_id = ''.join([path[-5:-4] for path in image_path_sequence])
			image = self.render_avatar_image(image_path_sequence, i)
			self.save_image(image, i)
