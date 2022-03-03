#include "GUI.hpp"
#include <iostream>

//COUCOU, je m'appelle Mohamed 

void menu(sf::RenderWindow *window){
    bool click = false;
    sf::Mouse mouse;
    sf::Mouse::Button lClick(sf::Mouse::Button::Left);
    while(click == false){

        sf::Event event;
        while (window->pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window->close();
        }
        if(mouse.isButtonPressed(lClick)){
            if(mouse.getPosition(*window).x >= 440 && mouse.getPosition(*window).x <= 840){
                if(mouse.getPosition(*window).y >= 500 && mouse.getPosition(*window).y <= 600){
                    click = true;
                }
            }
        }
        sf::RectangleShape button;
        button.setSize(sf::Vector2f(400,100));
        button.setPosition(440,500);
        button.setFillColor(sf::Color::Red);
        button.setOutlineColor(sf::Color::Black);
        button.setOutlineThickness(2);
        window->clear(sf::Color(150,100,100,255));
        window->draw(button);
        window->display();
    }
    
}