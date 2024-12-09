from bs4 import BeautifulSoup
import requests
import datetime


date = datetime.datetime.now().date()
time = datetime.datetime.now().time()
date = (str(date)+"_"+str(time)[0:8])
date = date.replace(":","_")


def save_slider_as_txt(films_in_slider_):
        
        while True:
            
            saving = input("Do you want to save movies in this section?\n0 - No save,\n1 - Save as txt")

            if saving == "1":
                
                for film in films_in_slider_:
                    name = film.find("strong",class_="poster-title").text
                    release_date = film.span.text
                    imdb_rate = film.find("span",class_="imdb").text

                    
                    with open("films_in_slider_"+date+".txt","a") as file:
                        file.write(f"Name of year: {name},Release Year: {release_date}, IMDB Rating: {imdb_rate}\n")
                file.close()
                break
    
            elif saving == "0":
                break
    
            else: 
                print("Wrong enter. Please Try Again.")


def save_category_as_txt(films):
        
        while True:
            
            saving = input("Do you want to save movies in this section?\n0 - No save,\n1 - Save as txt")

            if saving == "1":
                
                for film in films:
                    name = film.find("strong",class_="poster-title").text
                    release_year = film.find("div",class_="poster-meta").span.text
                    imdb_rate = film.find("span",class_="imdb").text

                    
                    with open("films_in_category_"+date+".txt","a") as file:
                        file.write(f"Name of year: {name}, IMDB Rating: {imdb_rate}, Release Year: {release_year}\n")
                file.close()
                print("Saved Succesfuly in "+"films_in_category_"+date+".txt")
                break
            elif saving == "0":
                break
    
            else: 
                print("Wrong enter. Please Try Again.")

    
    





def films_in_slider():
    main_page = requests.get("https://www.hdfilmcehennemi.nl/").text
    soup = BeautifulSoup(main_page,"lxml")
    slider = soup.find("div",class_="slider")
    films_in_slider_ = slider.find_all("div", class_="slider-slide")
    
    for film in films_in_slider_:
        name = film.find("strong",class_="poster-title").text
        release_date = film.span.text
        imdb_rate = film.find("span",class_="imdb").text
        print(f"Name of year: {name},Release Year: {release_date}, IMDB Rating: {imdb_rate}")
    
    save_slider_as_txt(films_in_slider_)

        




def films_in_choosed_category(category_url):
    category = requests.get(category_url).text
    category = BeautifulSoup(category,"lxml")
    films = category.find_all("a",class_="poster")

    for film in films:
        name = film.strong.text
        release_year = film.find("div",class_="poster-meta").span.text
        imdb_rate = film.find("span",class_="imdb").text

        print(f"Name of Movie: {name},IMDB Rate: {imdb_rate},Release Year: {release_year}")

    save_category_as_txt(films)



def films_for_category():
    request = input("Choose a category from below: \n1 - Documentary Category \n2 - Action Movies \n3 - Sci-fi Movies\n4 - Horror Movies\n5 - Movies in Slider\nWhat is your choose?: ")
    
    if request == "1":
        url = "https://www.hdfilmcehennemi.nl/tur/belgesel-filmlerini-izle-1/"
        films_in_choosed_category(url)
    
    elif request == "2":
        url = "https://www.hdfilmcehennemi.nl/tur/aksiyon-filmleri-izleyin-3/"
        films_in_choosed_category(url)
    
    elif request == "3":
        url = "https://www.hdfilmcehennemi.nl/tur/bilim-kurgu-filmlerini-izleyin-2/"
        films_in_choosed_category(url)
    
    elif request == "4":
        url = "https://www.hdfilmcehennemi.nl/tur/korku-filmlerini-izle-2/"
        films_in_choosed_category(url)
    
    elif request == "5":
        films_in_slider()
    
    else :
        print("Wrong entering")



if __name__ == "__main__":
    
    films_for_category()