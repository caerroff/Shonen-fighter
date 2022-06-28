#ifndef Characters_hpp
#define Characters_hpp

class Characters {
    
private:
    int tabSprites[100];
    int lengthTab = 20;
    int idCharacter;
    
public:
    Characters();
    void setTabSprites(int tabSprites[]);
    int getValueTabSprite(int indice) {return this->tabSprites[indice];}
    int getIdCharacter();
    void setIdCharacter(int id);
    int getLengthTab() {return lengthTab ;}
    
    void fillTab(int tab[]); 
        
};

#endif /* Characters_hpp */

