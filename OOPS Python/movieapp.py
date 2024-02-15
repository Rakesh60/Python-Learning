class movie:
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print('Movie name :',self.title)
        print('Hero :',self.hero)
        print('Heroine :',self.heroine)
        
list_of_movies=[]

while True:
    title=input('Enter movie name :')
    hero=input('Enter hero name :')
    heroine=input('Enter heroine name :')
    m=movie(title,hero,heroine)
    list_of_movies.append(m)
    print('Movie added Successfully')
    option=input('do you want to add one more movie [Yes|No]')
    
    if option.lower()=='no':
        break
    
print('All movie Information') 
print('#'*20)

for m in list_of_movies:
    m.info() 