from settings import *
from avatar import AvatarGenerator

# Number of avatars to generate

AVATARS = 100


def main():
	generator = AvatarGenerator(PATH)
	generator.generate_avatar(AVATARS)


if __name__ == '__main__':
	main()
