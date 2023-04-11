from settings import *


class Layer:
	def __init__(self, path):
		self.path = path
		self.rarity = 1.0

	def get_random_image_path(self, sequence=None):
		image_file_names = os.listdir(self.path)
		if sequence:
			for image in sequence:
				for img in image_file_names.copy():
					try:
						path = os.path.join(self.path, img)
						if path in EXCEPTIONS.get(image, []):
							image_file_names.remove(img)
					except ValueError:
						pass
		random_image_file_name = random.choice(image_file_names)
		return os.path.join(self.path, random_image_file_name)

	def should_generate(self):
		return random.random() < self.rarity
