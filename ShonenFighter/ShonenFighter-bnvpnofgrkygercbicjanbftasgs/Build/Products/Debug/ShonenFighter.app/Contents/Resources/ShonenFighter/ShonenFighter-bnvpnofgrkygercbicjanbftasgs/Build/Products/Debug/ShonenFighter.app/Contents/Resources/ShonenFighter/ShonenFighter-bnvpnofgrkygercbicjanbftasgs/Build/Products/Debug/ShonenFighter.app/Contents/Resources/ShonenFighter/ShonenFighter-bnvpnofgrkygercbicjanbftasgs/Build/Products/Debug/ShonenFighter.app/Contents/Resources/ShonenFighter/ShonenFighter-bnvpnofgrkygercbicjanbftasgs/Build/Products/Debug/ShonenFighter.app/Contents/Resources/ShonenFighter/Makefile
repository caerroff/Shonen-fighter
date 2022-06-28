all:
	@g++ -c *pp -lib/SFML-2.5.1/include -DSFML_STATIC
	@g++ *.o  -ISprites/* -Llib/SFML-2.5.1/lib -Lsrc/*.hpp  -DSFML_STATIC -lsfml-graphics -lsfml-window -lsfml-system -o ShonenFighter
	@mv *gch bin/
	@mv *.o bin/
	@./ShonenFighter